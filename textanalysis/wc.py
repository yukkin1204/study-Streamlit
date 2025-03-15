from pathlib import PurePath
import re
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud

FONT_PATH = PurePath(__file__).parent / "data/ipaexg.ttf"
POS_ID_FILE = PurePath(__file__).parent / "data/pos-id.txt"


# 単語分割
def get_tokens(text):
    sanitized = "".join(text.split())
    t = Tokenizer()
    tokens = [(w.surface, w.part_of_speech) for w in t.tokenize(sanitized)]
    return tokens


# ワードクラウド画像生成
def get_wordcloud(tokens, pos_list):
    # 指定の品詞の単語のみを抽出
    pos_joined = "|".join(pos_list)
    regexp = re.compile(f"^({pos_joined})")
    selected = [t[0] for t in tokens if regexp.search(t[1])]

    # 単語の頻度辞書の作成
    unique_words = list(set(selected))
    probs = {key: selected.count(key) for key in unique_words}

    # ワードクラウド画像生成
    word_cloud = WordCloud(
        font_path=FONT_PATH, background_color="lightgray", width=800, height=600, colormap="twilight"
    )
    img = word_cloud.fit_words(probs)

    return img.to_image()


# 品詞リストの取得
def get_pos_ids(file=POS_ID_FILE):
    with open(file) as fp:
        pos_ids = fp.readlines()
        pos_ids = [line.strip() for line in pos_ids]

    return pos_ids


if __name__ == "__main__":
    import sys
    from aozora import get_aozora
    from timer import timer  # type: ignore

    url = sys.argv[1]
    t = timer()
    text = get_aozora(url)
    t(f"Aozora: {len(text)} chars.")
    tokens = get_tokens(text)
    t(f"Tokenize: {len(tokens)} tokens.")
    img = get_wordcloud(tokens, ["名詞"])
    t(f"Wordcloud")
    img.save("./textanalysis/test.png")

    pos_ids = get_pos_ids()
    print("POS IDs: ", pos_ids)
