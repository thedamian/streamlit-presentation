import streamlit as st

st.title("👋 Hello, Streamlit!")

input_text = st.text_input("Enter some text")

st.write(f"You entered: {input_text}")

input_select = st.select_slider("Select a value", options=["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {input_select}")
