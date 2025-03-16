# LaTeXページ
import streamlit as st

st.header("LaTeX")

st.latex(r"E^2 = (mc^2)^2 + (pc)^2")
st.latex(r"I(t) = I\sin\phi(t)")
st.latex(
    r"""m\frac{d^2}{dt^2}\left< x \right> =
    - \left< \frac{\partial U}{\partial x} \right>"""
)
st.latex(
    r"""\left[S_Y, S_Z\right] = S_{Y} - S_{Z} =
    i\hbar S_X \lambda_s - \lambda_i = \frac{h}{mc} (1 - \cos\theta)"""
)
