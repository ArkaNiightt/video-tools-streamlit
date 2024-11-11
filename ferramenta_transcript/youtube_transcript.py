import streamlit as st
from ferramenta_transcript import fetch_video_transcript


def main():
    # Streamlit layout
    st.title("YouTube Video Transcript")
    video_url = st.text_input("Coloque a URL do vídeo:")

    if st.button("Pegar Transcrição"):
        if video_url:
            result = fetch_video_transcript(video_url)
            st.text_area("Video Transcript:", result, height=600)
        else:
            st.error("Please enter a valid YouTube URL.")
