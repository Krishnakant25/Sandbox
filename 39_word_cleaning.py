import streamlit as st
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from collections import Counter

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')

st.title("🧹 Clean My Text")

# Text input
text = st.text_area("Enter your text:")

# Cleaning options
lower = st.checkbox("Convert to lowercase")
remove_punct = st.checkbox("Remove punctuation")
remove_num = st.checkbox("Remove numbers")
remove_stop = st.checkbox("Remove stopwords")

# Emoji handling (dropdown)
emoji_option = st.selectbox(
    "Emoji Handling",
    ["Keep", "Remove", "Replace with [emoji]"]
)

# Clean button
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

    # Remove stopwords
    if remove_stop:
        words = word_tokenize(result)
        result = ' '.join([word for word in words if word.lower() not in stopwords.words('english')])

    # Handle emojis
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons 😊
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs 💌
        u"\U0001F680-\U0001F6FF"  # transport & map symbols 🚀
        u"\U0001F1E0-\U0001F1FF"  # flags 🏳️‍🌈
        "]+", flags=re.UNICODE)

    if emoji_option == "Remove":
        result = emoji_pattern.sub('', result)
    elif emoji_option == "Replace with [emoji]":
        result = emoji_pattern.sub('[emoji]', result)

    # Clean extra spaces
    result = re.sub(r'\s+', ' ', result).strip()

    # Show cleaned text
    st.subheader("✅ Cleaned Text:")
    st.write(result)

    # Word stats
    words = word_tokenize(result)
    st.write("**Word Count:**", len(words))

    if len(words) > 0:
        freq = Counter(words)
        st.write("**Top 3 Words:**", freq.most_common(3))
    else:
        st.write("No words left after cleaning.")