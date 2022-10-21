import streamlit as st
# import numpy as np
# import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.write(df)
# dataframeだと引数を指定できる
st.dataframe(df.style.highlight_max(axis=0))
st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項
```python
import streamlit as st
```

"""

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})


df = pd.DataFrame(
    np.random.rand(20, 4),
    columns = ['a', 'b', 'c', 'd']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon']
)
st.map(df)

st.write('Display Image')
img = Image.open('sample.png')
st.image(img, caption='name', use_column_width=True)

# if st.checkbox('Show Image'):
#     img = Image.open('sample.png')
#     st.image(img, caption='name', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください、',
    list(range(1,10))
)

'あなたの好きな数字は、', option, 'です。'

st.write('Intrrctive Widgets')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味は', text, 'です。'
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション:', condition

# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味は', text, 'です。'
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション:', condition

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('文字を書く')

expander1 = st.expander('お問合せ1')
expander1.write('問い合わせの回答')
expander2 = st.expander('お問合せ2')
expander2.write('問い合わせの回答')
expander3 = st.expander('お問合せ3')
expander3.write('問い合わせの回答')
expander4 = st.expander('お問合せ4')


import time
st.write('プログレスバーの表示')
'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # print(i)
    # latest_iteration = st.empty()
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.3)

'Done!!!!'