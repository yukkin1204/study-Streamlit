# 画像のポスタリゼーションページ
from PIL import Image, ImageFilter
import streamlit as st
from save import st_render

st.header(":rainbow[ポスタリゼーション]")

# keyにより、色数はst.session_state._image_colorsに保存される
colors = st.number_input("色数", min_value=2, max_value=256, value=256, step=1, key="image_colors")

if "image_upload" in st.session_state:
    # page1でアップロードされた画像を取得
    img = st.session_state.image_upload
    # 最頻値フィルタでポスタリゼーションの効果を高める
    mode_filter = ImageFilter.ModeFilter(size=7)
    filtered = img.filter(mode_filter)
    # 色数制限付きGIF変換
    poster = filtered.quantize(colors=colors)
    poster.filename = st.session_state.image_upload.filename
    # 画像の表示
    st.image(poster)

    # save.py で提供される画面の描画
    st_render(poster)
