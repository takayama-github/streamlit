import streamlit as st
import pandas as pd

df = pd.read_csv("./src/data/citizens/1.csv")
st.dataframe(df)
