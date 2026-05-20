import streamlit as st

st.title("Audio/Video with streamlit")

st.video("/home/tanmoy/Desktop/Phitron/Streamlit/Videos/Tanmoy - 2102079 - Logistic Regression.mp4")

vid = st.file_uploader("Select a vidoe",
                       type=["mp4"],
                       accept_multiple_files=True)

if vid:
    col = st.columns(len(vid))

    for i, per_video in enumerate(vid):
        with col[i]:
            st.video(per_video)
