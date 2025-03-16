# 画像のアップロードページ
from PIL import Image
import streamlit as st
from save import st_render

st.header(":rainbow[元画像]")


def onchange():
    # Imageオブジェクトに変換
    img = Image.open(st.session_state._image_upload)
    # ファイル名を補完
    img.filename = st.session_state._image_upload.name
    # main.pyからこの画像オブジェクトにアクセスできるように引き渡す
    st.session_state.image_upload = img


# 画像のアップロード
# keyにより、アップロードされたUploadedFileオブジェクトは、st.session_state._image_uploadに保存される
# また、コールバック関数としてonchangeが実行される
st.file_uploader("画像ファイルをアップロードしてください", key="_image_upload", on_change=onchange)

if "image_upload" in st.session_state:
    img = st.session_state.image_upload
    # 画像の表示
    st.image(img)

    # save.py で提供される画面の描画
    st_render(img)
