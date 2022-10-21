import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Material UI Button Designer",
    page_icon="🕹️",
)

st.image(
    "https://emojipedia-us.s3.amazonaws.com/source/skype/289/joystick_1f579-fe0f.png",
    width=125,
)

st.title('Video Translater')
st.text('動画をアップロードすると自動でAIが翻訳した字幕を生成し合成します。どの言語にも対応しています')
st.subheader(' ')
st.subheader('1. Video Select')
uploaded_files = st.file_uploader("Choose a Video file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

text_input = st.text_input(
        "use YouTube Video",
        placeholder="https://www.youtube.com/watch?v=..."
    )
st.subheader(' ')
st.subheader('2. Translate!')
option = st.selectbox(
    'あなたが翻訳する方向を教えてください、',
    # list(range(1,10))
    ('英語 → 日本語', 'ドイツ語 → 日本語')
)
st.button('Translate', width="200")
    # st.write('Why hello there')
    # st.write('Goodbye')
st.subheader(' ')
st.subheader('3.')

st.subheader(' ')
st.subheader('3.')

# https://docs.streamlit.io/library/api-reference/widgets/st.text_input

# Store the initial value of widgets in session state
# if "visibility" not in st.session_state:
#     st.session_state.visibility = "visible"
#     st.session_state.disabled = False


# col1, col2 = st.columns(2)

# with col1:
#     st.checkbox("Disable text input widget", key="disabled")
#     st.radio(
#         "Set text input label visibility 👉",
#         key="visibility",
#         options=["visible", "hidden", "collapsed"],
#     )
#     st.text_input(
#         "Placeholder for the other text input widget",
#         "This is a placeholder",
#         key="placeholder",
#     )

# with col2:
#     text_input = st.text_input(
#         "Enter some text 👇",
#         label_visibility=st.session_state.visibility,
#         disabled=st.session_state.disabled,
#         placeholder=st.session_state.placeholder,
#     )

#     if text_input:
#         st.write("You entered: ", text_input)