import streamlit as st
import pandas

def get_content ():

    left, center, right = st.columns(3)

    with center:
        st.image("images/home banner.png", width=800)
        st.image("images/ways.jpg", width=800)

    st.set_page_config(layout = "wide")

    left, center, right = st.columns([1.8, 0.2, 1.8])

    with left:
        st.image("images/script.jpg", width=600)
        st.image("images/vocabulary.jpg", width=600)
        st.image("images/grammar.jpg", width=600)
        st.image("images/listening.jpg", width=600)
        st.image("images/speaking.jpg", width=600)
        st.image("images/reading.jpg", width=600)
        st.image("images/writting.jpg", width=600)
        st.image("images/immersion.jpg", width=600)

    with right:
        st.image("images/japanese script.jpg", width=600)
        st.image("images/japanese vocabulary.jpg", width=600)
        st.image("images/japanese grammar.jpg", width=600)
        st.image("images/japanese listening.jpg", width=600)
        st.image("images/japanese speaking.jpg", width=600)
        st.image("images/japanese reading.jpg", width=600)
        st.image("images/japanese writting.jpg", width=600)
        st.image("images/japanese immersion.jpg", width=600)
