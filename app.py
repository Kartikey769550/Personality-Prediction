import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import time
import app1
import app2
import app3
img = Image.open('icon2.png')
img1 = Image.open('icon3.png')
img2 = Image.open('icon1.png')
st.set_page_config(page_title="Personality-Prediction", page_icon=img2, layout="wide")
hide_stream_lit_style ="""<style>#MainMenu{visibility: hidden;} footer {visibility: hidden}</style>"""
st.markdown(hide_stream_lit_style, unsafe_allow_html=True)

PAGES = {
    "Home": app1,
    "Personality-Prediction through Supervised": app2,
    "Personality-Prediction through UnSupervised": app3

}
st.sidebar.image(img1, width=260)
st.sidebar.subheader('Welcome')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
y = st.spinner(f'Loading {selection} ...')

with y:
    time.sleep(0.2)
    page.app()

x = st.sidebar.success(f"Successfully loaded {selection} ...")
time.sleep(0.2)
x.empty()
st.sidebar.info('© Prediction-Lab')
