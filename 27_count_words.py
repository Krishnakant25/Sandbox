from sklearn.feature_extraction.text import CountVectorizer

sentences = [
    "The cake was delicious and fresh",
    "The bread was fresh and soft",
    "Fresh cake and bread every day"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(sentences)

print(X)

print(vectorizer.get_feature_names_out())

print(X.toarray()) 