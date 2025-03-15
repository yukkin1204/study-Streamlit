from transformers import pipeline

MODEL = "Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime"
SENTIMENTS = "喜び、悲しみ、期待、驚き、怒り、恐れ、嫌悪、信頼".split("、")


# モデルの取得
def get_model(model=MODEL):
    pipe = pipeline("sentiment-analysis", model=model)
    return pipe


# 感情リストの取得
def get_sentiment(pipe, sentence):
    results = pipe(sentence)
    label_number = int(results[0]["label"][-1:])
    return SENTIMENTS[label_number]


if __name__ == "__main__":
    import sys
    from aozora import get_aozora, parse_text_into_sentences

    url = sys.argv[1]
    text = get_aozora(url)
    pipe = get_model()
    sentences = parse_text_into_sentences(text)
    emotions = [get_sentiment(pipe, sentence) for sentence in sentences]
    stats = {e: emotions.count(e) for e in SENTIMENTS}
    print(stats)
