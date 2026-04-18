from sklearn.feature_extraction.text import CountVectorizer

reviews = []
print("Enter 5 product reviews")
for i in range(5):
    review = input(f"review {i+1}: ")
    reviews.append(review)

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(reviews)
vocab = vectorizer.get_feature_names_out()
matrix = x.toarray()

print("\nVocabulary:")
print(vocab)

print("\nBag of Words Matrix:")
print(matrix)

