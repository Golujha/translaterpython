import streamlit as st
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source="auto",target="hi")

st.title("Lang Translator by Sadiq")

text = st.text_input("Enter any text")

translate = translator.translate(text)

st.write(translate)