import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
st.title('Mood Detector')
import emoji
import pyjokes

def display_sentiment_values(sentence):
    feeling = ''
    analyser = SentimentIntensityAnalyzer()
    sntiment = analyser.polarity_scores(sentence)
    st.write(sntiment)
    for key in sntiment:
        if sntiment[key] >= 0.5:
            feeling = key
    if feeling == "neg":
        st.write(emoji.emojize(":pensive_face:"))
        st.write("Don't wory tommorow will be fine and day aftr tommorow will be best")
        st.write(pyjokes.get_joke())

    elif feeling == "neu":
        st.write(emoji.emojize(":smiling_face_with_smiling_eyes:"))
        st.write("Okay,Be Happy")
        st.write(pyjokes.get_joke())
    elif feeling == "pos" or feeling == "compound":
        st.write(emoji.emojize(":smiling_face_with_heart-eyes:"))
        st.write("Good keep it up")

sentence=st.text_input('Tell me about today ?...')
display_sentiment_values(sentence)
