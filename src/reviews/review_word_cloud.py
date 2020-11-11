import os
import sys
import json
from typing import List, Dict
from tempfile import mkstemp
import asyncio
import aiofiles
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# 项目目录
project_dir = os.path.abspath(os.path.join(os.getcwd(), "../.."))
# 把当前python程序的项目目录的绝对路径加入到环境变量PYTHON_PATH中
sys.path.append(project_dir)

from src.mock.mock import mock_word_cloud

app = FastAPI()


# 声明参数模型
class Item(BaseModel):
    code: str
    answer: Dict
    scores: Dict


async def review_word_cloud(code: str, answer: Dict, scores: Dict, debug=False):
    # 将code写入文件
    tmp_fp, tmp_file_name = mkstemp(suffix=".py", dir='.', text=True)
    async with aiofiles.open(tmp_file_name, "w") as f:
        await f.write(code)
    if debug:
        print(f'tmp_fp-->{tmp_fp} === tmp_file_name-->{tmp_file_name}')

    # 创建子进程执行代码
    cmd = ['python', '-sB', tmp_file_name]
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        close_fds=True
    )

    # 评测词云，打分
    score = 0
    while process.returncode is None:
        try:
            line_data: bytes = await asyncio.wait_for(process.stdout.readline(), 2)
            if b'e485c73f5dd07c29' in line_data:
                review_data: str = line_data.decode('u8')
                review_data: Dict = json.loads(review_data)
                if debug:
                    print(f'debug:review_data-->{review_data}')
                for key, value in answer.items():
                    # 字符串或数值，则比较值是否相等
                    if isinstance(value, (str, int)):
                        tmp_score = scores.get(key) if value == review_data.get(key, None) else 0
                    elif isinstance(value, List):
                        tmp_score = scores.get(key) if set(value) == set(review_data.get(key, None)) else 0
                    elif isinstance(value, Dict):
                        tmp_score = scores.get(key) if value == review_data.get(key, None) else 0
                    else:
                        tmp_score = 0
                    score += tmp_score
            else:
                if debug:
                    print(f'debug:line_data-->{line_data.decode("u8")}')  # 打印其他数据
        except asyncio.TimeoutError:
            lines_data: bytes = await asyncio.wait_for(process.stdout.read(1024), 2)
            if debug:
                print(f'debug:lines_data-->{lines_data.decode("u8")}')  # 数据不是多行，不走这里

    # 还原环境，删除临时文件
    os.remove(tmp_file_name)

    # 返回结果
    result = {
        'status': 200,
        'score': score,
    }

    # 程序异常情况
    out, err = await process.communicate()
    if err:
        result['status'] = 400
        result['error'] = err.decode('u8')

    if debug:
        print(f'debug:result-->{result}')
    return result


@app.post("/reviews/wordcloud")
async def read_root(item: Item):
    # 是否debug
    debug = True
    result = await review_word_cloud(code=item.code, answer=item.answer, scores=item.scores, debug=debug)
    return result


if __name__ == '__main__':
    # 项目目录
    project_dir = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    # 替换词云源代码
    mock_word_cloud(project_dir)
    # 运行API
    uvicorn.run(app='review_word_cloud:app', host="127.0.0.1", port=8000, reload=True, debug=True)
