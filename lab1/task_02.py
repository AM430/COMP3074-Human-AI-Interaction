import math
from collections import defaultdict

import nltk
from joblib import dump, load
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("wordnet")
nltk.download("stopwords")

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

text = "The movies were really good, and the actors were excellent."
documents = {
    "doc1": "This movie was good and funny.",
    "doc2": "This movie was boring.",
    "doc3": "The acting was good.",
}
processed_documents = {}
idf = {}


def preprocess(text):
    tokens = word_tokenize(text.lower())

    clean_tokens = [
        token for token in tokens if token.isalpha() and token not in stop_words
    ]

    lemmas = [lemmatizer.lemmatize(token) for token in clean_tokens]

    return lemmas


print(preprocess(text))
# TF
for doc_id, text in documents.items():
    processed_documents[doc_id] = preprocess(text)

print(processed_documents)
# DF
document_frequency = defaultdict(int)

for tokens in processed_documents.values():
    unique_terms = set(tokens)

    for term in unique_terms:
        document_frequency[term] += 1

print(dict(document_frequency))

N = len(processed_documents)
for term, df in document_frequency.items():
    idf[term] = f"{math.log(N / df): .3f}"
for term, score in idf.items():
    print(term, score)

vocabulary = {}

for i, term in enumerate(sorted(idf.keys()), start=1):
    term_id = f"t{i:03d}"

    vocabulary[term] = {"term_id": term_id, "idf": idf[term]}
for term, info in vocabulary.items():
    print(term, info)

dump(vocabulary, "lab1/vocabulary.joblib")

loaded_vocabulary = load("lab1/vocabulary.joblib")
print(loaded_vocabulary)
