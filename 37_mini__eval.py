import streamlit as st
import spacy
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

st.title("🔍 Stem vs Lemma Accuracy Tester")

words_input = st.text_input("Enter comma-separated words:")
if words_input:
    words = [w.strip() for w in words_input.split(",") if w.strip()]
    porter = PorterStemmer()
    wn = WordNetLemmatizer()
    nlp = spacy.load("en_core_web_sm")

    correct_stem = 0
    correct_lemma = 0

    st.markdown("| Word | Porter Stem | Lemma (spaCy) | Stem Correct? | Lemma Correct? |")
    st.markdown("|------|--------------|---------------|----------------|-----------------|")

    for word in words:
        stem = porter.stem(word)
        lemma = nlp(word)[0].lemma_

        col1, col2 = st.columns(2)
        stem_ok = col1.checkbox(f"✅ Is stem '{stem}' for '{word}' correct?", key=f"stem_{word}")
        lemma_ok = col2.checkbox(f"✅ Is lemma '{lemma}' for '{word}' correct?", key=f"lemma_{word}")

        if stem_ok:
            correct_stem += 1
        if lemma_ok:
            correct_lemma += 1

        st.markdown(f"| {word} | {stem} | {lemma} | {'✅' if stem_ok else '❌'} | {'✅' if lemma_ok else '❌'} |")

    total = len(words)
    if total > 0:
        st.success(f"🔧 Stem Accuracy: {correct_stem}/{total} = {round((correct_stem/total)*100)}%")
        st.success(f"🧠 Lemma Accuracy: {correct_lemma}/{total} = {round((correct_lemma/total)*100)}%")