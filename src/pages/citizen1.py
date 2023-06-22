import streamlit as st
import pandas as pd

form = st.form(key='data_form')
with form:
    min_limit = st.number_input('下限年齢', step=1, value=0, min_value=0)
    max_limit = st.number_input('上限年齢', step=1, value=100, max_value=100)
    descending = not st.checkbox('降順')

    display_btn = st.form_submit_button('表示')

    if display_btn:
        df = pd.read_csv("./src/data/citizens/1.csv")
        df = df[df['年齢'] >= min_limit]
        df = df[df['年齢'] <= max_limit]
        df = df.sort_values('年齢', ascending=descending)
        st.dataframe(df)
