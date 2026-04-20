import streamlit as st
import nltk
from nltk.stem import LancasterStemmer, PorterStemmer, WordNetLemmatizer
import spacy

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

ps = PorterStemmer()
ls = LancasterStemmer()
lemmatizer = WordNetLemmatizer()
nlp = spacy.load("en_core_web_sm")
st.title("🔁 Stemming vs Lemmatization")

text = st.text_input("Enter a sentence or list of words:")

if st.button("Process"):
    words = nltk.word_tokenize(text)

    st.markdown("### Results:")
    st.markdown("| Word | Porter Stem | Lancaster Stem | Lemma (NLTK) | Lemma (spaCy) |")
    st.markdown("|------|--------------|----------------|---------------|----------------|")
    for word in words:
        doc = nlp(word)
        spacy_lemma = doc[0].lemma_
        row = f"| {word} | {ps.stem(word)} | {ls.stem(word)} | {lemmatizer.lemmatize(word)} | {spacy_lemma} |"
        st.markdown(row)