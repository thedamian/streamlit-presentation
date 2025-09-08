import pandas as pd
import streamlit as st

st.set_page_config(page_title="📊 Basic Pandas Example", layout="wide")
st.title("📊 Basic Pandas Example")
st.markdown("_Prototype v04.01")

# display data
data = pd.read_excel("ImportantFinancialStuff.xlsx")
st.dataframe(data)