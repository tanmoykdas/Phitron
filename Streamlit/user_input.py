import streamlit as st

st.title("YOUR NAME",anchor=False)

name = st.text_input("Enter you full name:")
st.markdown(f"this person name is :red[{name}]")

age = st.number_input("Enter your age", value=None, placeholder="your age")
