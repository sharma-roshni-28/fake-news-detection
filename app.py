import streamlit as st

st.title("Fake News Detection System")

news = st.text_area("Enter News Here")

if st.button("Check News"):

    if "shocking" in news.lower():
        st.error("Fake News Detected")
    else:
        st.success("Real News")