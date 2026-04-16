import streamlit as st

st.title("Login page")

email = st.text_input("Enter you email adress:", value=None, placeholder="abc@gmial.com")

st.divider()

password = st.text_input("Enter your password:", value=None, type="password")

st.divider()

pressed = st.button("login",type="primary")

if pressed:
    st.write("Login Sucessful!")