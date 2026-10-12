import math
from collections import Counter

import nltk
import numpy as np
from joblib import load
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("wordnet")
nltk.download("stopwords")

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))
documents = {
    "doc1": "This movie was good and funny.",
    "doc2": "This movie was boring.",
    "doc3": "The acting was good.",
}
processed_documents = {
    "doc1": ["movie", "movie", "good", "funny"],
    "doc2": ["movie", "boring"],
    "doc3": ["acting", "good"],
}
vocabulary = load("lab1/vocabulary.joblib")
terms = sorted(vocabulary.keys())

document_term_matrix = {}

print("processed_documents:", processed_documents)
print("vocabulary:", vocabulary)


def preprocess(text):
    tokens = word_tokenize(text.lower())

    clean_tokens = [
        token for token in tokens if token.isalpha() and token not in stop_words
    ]

    lemmas = [lemmatizer.lemmatize(token) for token in clean_tokens]

    return lemmas


def get_weight(count, method):
    if method == "raw":
        return count

    if method == "binary":
        return 1 if count > 0 else 0

    if method == "log":
        return math.log(1 + count)

    raise ValueError("Unknown weighting method")


def build_matrix(processed_documents, vocabulary, method):
    terms = sorted(vocabulary.keys())

    matrix = {}

    for doc_id, tokens in processed_documents.items():
        counts = Counter(tokens)

        matrix[doc_id] = {}

        for term in terms:
            matrix[doc_id][term] = get_weight(counts[term], method)

    return matrix


raw_matrix = build_matrix(processed_documents, vocabulary, "raw")

binary_matrix = build_matrix(processed_documents, vocabulary, "binary")

log_matrix = build_matrix(processed_documents, vocabulary, "log")

print("RAW")
for doc_id, row in raw_matrix.items():
    print(doc_id, row)

print("\nBINARY")
for doc_id, row in binary_matrix.items():
    print(doc_id, row)

print("\nLOG")
for doc_id, row in log_matrix.items():
    print(doc_id, row)

terms = sorted(vocabulary.keys())
doc_ids = list(raw_matrix.keys())

raw_np = np.array([[raw_matrix[doc_id][term] for term in terms] for doc_id in doc_ids])

print("Terms:", terms)
print("Documents:", doc_ids)
print(raw_np)
