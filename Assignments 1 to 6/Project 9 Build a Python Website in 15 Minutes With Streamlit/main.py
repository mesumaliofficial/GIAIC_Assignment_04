import streamlit as st

st.title("Simple Streamlit Website")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}!")
else:
    st.write("Please enter your name to be greeted.")
