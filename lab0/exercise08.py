"""Find a set of documents and try to download/parse them.  What is the proportion of
nouns vs. verbs vs. adjectives in an average novel?"""

import nltk
from nltk.corpus import gutenberg

nltk.download("gutenberg")
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")
nltk.download("universal_tagset")
nltk.download("punkt_tab")

# print(gutenberg.fileids())

text = gutenberg.raw("austen-emma.txt")
tokens = nltk.word_tokenize(text)
words = [word for word in tokens if word.isalpha()]
tagged = nltk.pos_tag(words, tagset="universal")

noun_count = 0
verb_count = 0
adj_count = 0

for word, tag in tagged:
    if tag == "NOUN":
        noun_count += 1
    elif tag == "VERB":
        verb_count += 1
    elif tag == "ADJ":
        adj_count += 1

total = noun_count + verb_count + adj_count
print("Total words:", total)

print(
    f"Nouns: {noun_count / total:.2%}",
    noun_count,
)
print(
    f"Verbs: {verb_count / total:.2%}",
    verb_count,
)
print(
    f"Adjectives: {adj_count / total:.2%}",
    adj_count,
)

print(f"Nouns in text: {noun_count / len(words):.2%}")
print(f"Verbs in text: {verb_count / len(words):.2%}")
print(f"Adjectives in text: {adj_count / len(words):.2%}")
