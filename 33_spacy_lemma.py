import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("The children are running to the playground.")
print([token.lemma_ for token in doc])