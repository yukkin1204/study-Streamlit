from time import monotonic, sleep


# それぞれの操作にかかった時間を計測
def timer():
    start = monotonic()

    def inner(message):
        print(f"{message}: {monotonic() - start:.2f}")

    return inner


if __name__ == "__main__":
    t = timer()
    t("hello world")
    sleep(3)
    t("hello world 2")
    sleep(2)
    t("hello world 3")
