import pandas as pd
import streamlit as st

st.set_page_config(page_title="📊 Basic Pandas Example", layout="wide")
st.title("📊 Basic Pandas Example")

# display data
data = pd.read_excel("ImportantFinancialStuff.xlsx")
st.dataframe(data)