import streamlit as st
import pandas as pd

col1, col2 = st.columns(2)
df = pd.read_csv("./src/data/employees/1.csv")

with col1:
    st.dataframe(df)

with col2:
    st.table(df)
