import streamlit as st
import re

st.title("🔗 URL and 📧 Email Cleaner")

# Text input for user to paste text
text = st.text_area("Enter text with URLs or emails")

# Options for cleaning
remove_url = st.checkbox("Remove URLs")
remove_email = st.checkbox("Remove Emails")

if st.button("Clean Text"):
    result = text

    # Remove URLs (http, https, www)
    if remove_url:
        result = re.sub(r"http\S+|https\S+|www\S+", "", result)

    # Remove email addresses
    if remove_email:
        result = re.sub(r"\b\S+@\S+\.\S+\b", "", result)

    # Show cleaned text output inside the button block
    st.subheader("Cleaned Text:")
    st.write(result)
