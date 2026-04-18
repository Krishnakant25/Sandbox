from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    "I Love Python and AI",
    "Python is great for Data Science",
    "AI will shape the future"
]

ventorizer = TfidfVectorizer()
x = ventorizer.fit_transform(corpus)


print('\nVocabulary Indexes')
print(ventorizer.vocabulary_)
print('\ntf-idf values')
print(x)
print('\ntf-idf values in the matrix form:')
print(x.toarray())