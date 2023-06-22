import streamlit as st
import pandas as pd

df = pd.read_csv("./src/data/citizens/3.csv")
st.dataframe(df)
