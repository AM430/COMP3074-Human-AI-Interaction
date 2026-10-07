"""Look at the stopword list (you can print stopwords.words(‘English’)): what problems
do you think having a fixed stopword list could cause? How would you overcome them?
Can you build a better stopword list?"""

import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

english_stopwords = stopwords.words("english")
custom_stopwords = set(english_stopwords)

custom_stopwords.discard("not")
custom_stopwords.discard("no")
custom_stopwords.discard("nor")

# print(english_stopwords)

sentence = "I do not like this movie"

words = sentence.lower().split()

filtered_words = [word for word in words if word not in custom_stopwords]

print("Original:", words)
print("Filtered:", filtered_words)
