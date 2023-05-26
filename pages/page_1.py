import streamlit as st
st.write('メインページのコードです')
code = '''
import streamlit as st
from PIL import Image
st.title('サンプルアプリ')
st.header('ヘッダー')
st.subheader('サブヘッダー')
st.write('文字列　　') # markdown
st.caption('これはテストアプリです')
           
image = Image.open('./data/blue.png')
st.image(image, width=400)

# https://docs.streamlit.io/library/api-reference　　（公式サイト）
'''
st.code(code, language='python')
