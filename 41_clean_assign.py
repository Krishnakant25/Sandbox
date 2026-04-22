import streamlit as st
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

st.title("🧹 Clean My Text")

# Text input
text = st.text_area("Enter your Text:")

# Cleaning options
lower = st.checkbox("Convert to LowerCase")
remove_punct = st.checkbox("Remove Punctuation")
remove_num = st.checkbox("Remove Numbers")
remove_stop = st.checkbox("Remove StopWords")

# Button to clean text
if st.button("Clean Text"):
    result = text

    # Convert to lowercase
    if lower:
        result = result.lower()

    # Remove punctuation
    if remove_punct:
        result = ''.join([ch for ch in result if ch not in string.punctuation])

    # Remove numbers
    if remove_num:
        result = ''.join([ch for ch in result if not ch.isdigit()])

    # Tokenize words
    words = word_tokenize(result)

    # Handle stopwords
    if remove_stop:
        stop_words = set(stopwords.words('english'))
        filtered = [word for word in words if word.lower() not in stop_words]
        removed = [word for word in words if word.lower() in stop_words]
        removed_percent = (len(removed) / len(words)) * 100
        result = ' '.join(filtered)
    # Calculate average word length
        avg_length = sum(len(word) for word in words) / len(words)

    # Display results
    st.subheader("✅ Cleaned Text:")
    st.write(result)

    st.write(f"📏 **Average Word Length:** {avg_length:.2f}")

    if remove_stop:
        st.write(f"🧾 **Percentage of Stopwords Removed:** {removed_percent:.2f}%")