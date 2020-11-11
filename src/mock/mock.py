import shutil
import sys
from pathlib import Path
from typing import Union


def mock_word_cloud(project_work_space: Union[Path, str]) -> None:
    src = Path(project_work_space, "src/mock/codes/code_wc.py")
    path_key_word = "packages"
    for i in sys.path:
        if path_key_word in i:
            dest_dir_path = Path(i, "wordcloud")
            dest_file_path = dest_dir_path / "wordcloud.py"
            break
    else:
        raise FileNotFoundError("Can't find site packages path")
    dest_dir_path.mkdir(parents=True, exist_ok=True)
    if dest_file_path.exists():
        dest_file_path.unlink()
    shutil.copyfile(src, dest_file_path)
    print("review_wordcloud 后台文件生成成功！")


if __name__ == "__main__":
    # 测试
    mock_word_cloud("/Users/zhou/Downloads/ddc_oj")
