import requests

url = "http://127.0.0.1:8000/reviews/wordcloud"

data = {
    'code': """import wordcloud
c = wordcloud.WordCloud()
txt = 'I have a good friend, and her name is Li Hua. We have become friends for about two years. She is very kind. When I step into the classroom for the first time, she helps me to get familiar with the strange environment. The most important thing is that we share the same interest, so we have a lot in common. '
c = c.generate(txt)
img = c.to_image()
print(123)
# img.show()""",
    'answer': {
        'words': {'good': 1, 'friend': 2, 'name': 1, 'Li': 1, 'Hua': 1, 'become': 1, 'two': 1, 'years': 1,
                  'kind': 1,
                  'step': 1, 'classroom': 1, 'first': 1, 'time': 1, 'helps': 1, 'familiar': 1, 'strange': 1,
                  'environment': 1, 'important': 1, 'thing': 1, 'share': 1, 'interest': 1, 'lot': 1, 'common': 1},
        'width': 400,
        'height': 200,
        'min_font_size': 4,
        'max_font_size': 26,
        'font_step': 1,
        'font_path': 'DroidSansMono.ttf',
        'max_words': 200,
        'stopwords': ['what', "i'll", "won't", 'than', 'same', 'at', "they'll", "there's", 'should', 'through',
                      'was',
                      'for', 'else', 'while', "they've", 'own', 'if', 'has', 'most', 'there', 'or', 'the', 'hers',
                      'during', "that's", "they'd", 'as', 'com', "how's", 'him', "what's", 'yourself', 'he',
                      "hadn't",
                      "shouldn't", 'few', 'under', "he'd", 'all', 'myself', 'once', "we're", 'your', 'shall', 'an',
                      'r',
                      "mustn't", "i'd", 'with', 'ours', 'such', 'which', "who's", 'about', 'she', 'whom', 'since',
                      'where', 'yourselves', 'down', 'some', 'below', "we've", 'from', 'its', 'to', 'am', 'just',
                      'above', "you're", "let's", 'me', "she's", 'not', 'too', 'both', 'very', 'any', 'like',
                      'against',
                      'then', 'over', 'ever', 'are', 'who', 'also', 'by', "you'd", 'our', 'nor', 'of', 'between',
                      'out',
                      "wouldn't", 'why', 'does', "doesn't", 'his', 'each', 'would', 'on', 'itself', 'ought',
                      'therefore', 'how', 'more', "hasn't", "he's", 'get', 'is', 'but', 'here', 'further', "we'd",
                      'only', 'http', 'do', 'yours', 'her', "they're", 'until', 'however', 'himself', 'be', 'could',
                      "she'd", 'a', 'it', 'them', "why's", 'www', 'up', 'other', 'themselves', "he'll", 'this',
                      'so',
                      'they', "don't", 'their', 'being', 'into', 'after', "where's", "shan't", 'because', 'have',
                      'my',
                      'again', "couldn't", 'off', 'in', 'we', 'having', "isn't", "i'm", 'ourselves', "it's", 'you',
                      "wasn't", "i've", "you'll", 'were', "when's", 'had', 'cannot', 'i', "haven't", 'those',
                      "aren't",
                      'no', 'hence', 'been', 'k', "here's", "didn't", 'before', "we'll", 'doing', "weren't",
                      'herself',
                      'did', 'can', 'that', 'and', 'theirs', "can't", 'otherwise', "you've", "she'll", 'these',
                      'when'],
        'mask': '6adf97f83acf6453d4a6a4b1070f3754',
        'background_color': 'black'
    },
    'scores': {
        'words': 5,
        'width': 5,
        'height': 10,
        'min_font_size': 10,
        'max_font_size': 10,
        'font_step': 10,
        'font_path': 10,
        'max_words': 10,
        'stopwords': 10,
        'mask': 10,
        'background_color': 10
    },
}

r = requests.post(url=url, json=data)
print(r.json())
