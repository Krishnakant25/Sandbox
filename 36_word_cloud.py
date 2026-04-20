#Build a Streamlit app that: Accepts a paragraph of text, Lemmatizes or stems each word, Displays a WordCloud of the root forms
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import spacy
import nltk
from nltk.stem import PorterStemmer

# Download tokenizer
nltk.download('punkt')

st.title("☁️ Root Word Cloud Generator")

# User input
text = st.text_area("Enter your text:")

# Method selection
method = st.radio("Choose method:", ["Stemming", "Lemmatization"])

if text:
    # Tokenize words
    words = nltk.word_tokenize(text)
    ps = PorterStemmer()
    nlp = spacy.load("en_core_web_sm")

    roots = []
    for word in words:
        if word.isalpha():  # ignore punctuation/numbers
            if method == "Stemming":
                roots.append(ps.stem(word.lower()))
            else:
                roots.append(nlp(word.lower())[0].lemma_)

    # Join roots for WordCloud
    freq = " ".join(roots)
    wc = WordCloud(width=800, height=400, background_color="white").generate(freq)

    # Display WordCloud
    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)