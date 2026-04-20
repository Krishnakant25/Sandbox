import streamlit as st
import nltk
import spacy
from nltk.stem import LancasterStemmer, PorterStemmer, WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

st.title("🧪 NLP Stem & Lemma Analyzer")

# User input
text = st.text_area("Enter a paragraph of text:")

if text:
    # Initialize tools
    ps = PorterStemmer()
    ls = LancasterStemmer()
    wn = WordNetLemmatizer()
    nlp = spacy.load("en_core_web_sm")

    # Process text with spaCy
    doc = nlp(text)

    # Table headers
    st.markdown("### 📊 Word Analysis Table")
    st.markdown("| Word | POS | Porter Stem | Lancaster Stem | NLTK Lemma | spaCy Lemma | Different? |")
    st.markdown("|------|-----|--------------|----------------|-------------|---------------|------------|")

    # Analyze each word
    for token in doc:
        if token.is_alpha:  # Skip punctuation/numbers
            word = token.text
            pos = token.pos_
            porter = ps.stem(word)
            lancaster = ls.stem(word)
            lemma_nltk = wn.lemmatize(word.lower())
            lemma_spacy = token.lemma_

            # Mark difference if any result doesn’t match the original word
            diff = "✅" if len({word.lower(), porter, lancaster, lemma_nltk, lemma_spacy}) > 1 else "❌"

            st.markdown(f"| {word} | {pos} | {porter} | {lancaster} | {lemma_nltk} | {lemma_spacy} | {diff} |")