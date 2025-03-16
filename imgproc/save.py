# 画像の変換とダウンロード
from io import BytesIO
from pathlib import PurePath
from PIL import Image


# 画像フォーマットの一覧を取得
def get_extensions():
    return list(Image.registered_extensions().keys())


# Imageオブジェクトをバイナリストリームとしてバッファに保存する
def image_to_bytes(pil_image, extension=".png"):
    filename = PurePath(pil_image.filename).with_suffix(extension).name
    buf = BytesIO()
    try:
        pil_image.save(buf, format=Image.registered_extensions()[extension])
        buf_bytes = buf.getvalue()
    except Exception as e:
        buf_bytes = None

    return (filename, buf_bytes)


# 画面描画（page1〜3.pyから呼び出される）
def st_render(pil_image):
    import streamlit as st

    with st.sidebar:
        st.divider()
        with st.popover("画像フォーマットを選択"):
            extension = st.radio(label="変換先フォーマット", options=get_extensions(), index=None, horizontal=True)

        if extension:
            filename, buffer = image_to_bytes(pil_image, extension)
            if buffer is None:
                st.error(f"{extension}への変換ができません。")
            else:
                st.download_button(f"`{extension}` としてダウンロード（`{filename}`）", buffer, file_name=filename)


if __name__ == "__main__":
    import sys

    print(get_extensions())

    img = Image.open(sys.argv[1])
    filename, buf = image_to_bytes(img, extension=".jpg")
    print(f"Filename: {img.filename} to {filename}.")
