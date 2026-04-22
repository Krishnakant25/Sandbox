# challenge_custom_stopwords.py
import streamlit as st
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('stopwords')

st.title("🛠️ Custom Stopword Remover")

text = st.text_area("Enter your text:")
custom_stop_input = st.text_input("Enter custom stopwords (comma-separated):")

if st.button("Remove Stopwords"):
    base_stopwords = set(stopwords.words('english'))
    custom_stopwords = [word.strip().lower() for word in custom_stop_input.split(",") if word]

    all_stops = base_stopwords.union(set(custom_stopwords))

    tokens = word_tokenize(text)
    filtered = [word for word in tokens if word.lower() not in all_stops]

    st.subheader("Filtered Text:")
    st.write(" ".join(filtered))