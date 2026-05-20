import streamlit as st

st.title("Image selection",anchor=None)
st.image("/home/tanmoy/Desktop/Phitron/Streamlit/Images/20241206_164239.jpg")
images = st.file_uploader("Select your image",
                          type = ['jpg', 'jpeg', 'png'],
                          accept_multiple_files=True)

if images:
    cols = st.columns(len(images))
    for i, per_image in enumerate(images):
        with cols[i]:
            st.image(per_image)