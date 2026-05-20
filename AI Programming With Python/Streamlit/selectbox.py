import streamlit as st

st.title("Profession selection")
st.divider()

selected = st.selectbox("Choose your profession: ", 
                        ("Student", "Doctor", "Engineer"),
                        index=None, placeholder="which one define you",
                        accept_new_options=True)
st.write(f"Your choosen profession is {selected}")