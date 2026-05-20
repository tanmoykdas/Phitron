import streamlit as st

st.title("Calculator", anchor=None)

a = st.number_input("Enter your first number",
                     value=None, placeholder="A")

b = st.number_input("Enter your second number",
                     value=None, placeholder="B")

select = st.selectbox("which operation you want to perform?",
                      ["+", "-", "*", "/"], index=None)

pressed = st.button("Calculate", type="primary")

if pressed:
    if (select == "+"):
        ans = a + b
    elif (select == "-"):
        ans = a - b
    elif (select == "*"):
        ans = a * b
    else:
        ans = a / b
    
    st.write(f"Your ans is: {ans}")