#Asignment on creating an APP to clean it via checkbox
import streamlit as st
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')
st.title("Clean My Text")
text = st.text_area("Enter your Text: ")
lower = st.checkbox("Convert to LowerCase")
remove_punct = st.checkbox("Remove Punctuation")
remove_num = st.checkbox("Remove Numbers")
remove_stop = st.checkbox("Remove StopWords")
if st.button("Clean Text"):
    result = text
    if lower:
        result = result.lower()
    if remove_punct:
        result = ''.join([ch for ch in result if ch not in string.punctuation])
    if remove_num:
        result = ''.join([ch for ch in result if not ch.isdigit()])
    if remove_stop:
        words = word_tokenize(result)
        filtered = [word for word in words if word.lower() not in stopwords.words('english')]
        result = ' '.join(filtered)
    st.subheader("Cleaned Text")
    st.write(result)