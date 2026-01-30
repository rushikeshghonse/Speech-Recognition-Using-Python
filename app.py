import streamlit as st
from speech_utils import recognize_speech

st.set_page_config(
    page_title="Speech Recognition App",
    page_icon="🎤"
)

st.title("🎤 Speech Recognition App")
st.write("Click the button and speak. Your speech will be converted to text.")

if st.button("🎙️ Start Listening"):
    with st.spinner("Listening..."):
        speech_text = recognize_speech()
    
    st.subheader("You said:")
    st.info(speech_text)
