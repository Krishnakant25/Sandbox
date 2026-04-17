from sklearn.feature_extraction.text import CountVectorizer
import streamlit as st
import pandas as pd

st.title("Bag of words visualiser")

sentence = st.text_area("Enter your Text here!!")

if sentence.strip() == "":
        st.warning("Please enter some text first!")
else:
        # 1. Initialize the vectorizer
        vectorizer = CountVectorizer()
        
        # 2. Fit and transform the text (wrapped in a list)
        x = vectorizer.fit_transform([sentence])
        
        # 3. Get the unique words (column headers)
        words = vectorizer.get_feature_names_out()
        
        # 4. Convert the sparse matrix to a dense array and then a DataFrame
        df = pd.DataFrame(x.toarray(), columns=words)
        
        # 5. Display the output
        st.subheader("Word Count Results")
        st.dataframe(df)
        
        # Optional: Show a bar chart of the word frequencies
        st.subheader("Frequency Chart")
        st.bar_chart(df.T)