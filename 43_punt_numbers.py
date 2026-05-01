import string
text = "Hello!!!, I have 2 cats."
cleaned = ''.join([char for char in text if char not in string.punctuation and not char.isdigit()])
print(cleaned)

#Alternative Method
import re
cleaned_1 = re.sub(r'[^a-zA-Z\s]', '', text)
print(cleaned_1)