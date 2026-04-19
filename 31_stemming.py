from nltk.stem import PorterStemmer, LancasterStemmer

porter = PorterStemmer()
lancaster = LancasterStemmer()

print(porter.stem("running"))     # run
print(lancaster.stem("running"))  # run