import streamlit as st
from PIL import Image

st.title('サンプルアプリ')
st.caption('これはテストアプリです')
st.title('タイトル')
st.header('ヘッダー')
st.subheader('サブヘッダー')
st.write('文字列') # markdown
           
image = Image.open('./data/blue.png')
st.image(image, width=400)
