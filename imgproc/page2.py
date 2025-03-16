# 画像のリサイズページ
from PIL import Image, ImageOps
import streamlit as st
from save import st_render

st.header(":rainbow[リサイズ]")

# keyにより、倍率はst.session_state._image_scaleに保存される
num = st.slider("倍率", min_value=0.1, max_value=2.0, value=1.0, step=0.1, key="image_scale")

if "image_upload" in st.session_state:
    # page1でアップロードされた画像を取得
    img = st.session_state.image_upload
    # 画像のリサイズ
    resized = ImageOps.scale(img, num)
    resized.filename = img.filename
    # 画像の表示
    st.image(resized, use_container_width="never")

    # save.py で提供される画面の描画
    st_render(resized)
