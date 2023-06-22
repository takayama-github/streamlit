import streamlit as st
import pandas as pd

df = pd.read_csv("./src/data/citizens/2.csv")
st.table(df)
