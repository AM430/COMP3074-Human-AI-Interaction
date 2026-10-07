"""[⋆] You can use the vocab() method to access the vocabulary of a Text object in the form
of a dictionary, where the key is the token and the value is its frequency in a given text.
Use this to build a function topN(S,N) that, given as input a string of characters S and a
number N, returns the top N tokens with decreasing frequency."""

import nltk
from nltk.tokenize import word_tokenize

# text = "cat dog cat bird dog cat fish bird cat"

# tokens = word_tokenize(text)
# print(tokens)

# nltk_text = nltk.Text(tokens)
# vocab = nltk_text.vocab()
# print(vocab)

# print("Top 3 tokens:", vocab.most_common(3))


# def topN(S, N):
#     tokens = word_tokenize(S)
#     nltk_text = nltk.Text(tokens)
#     vocab = nltk_text.vocab()


#     return vocab.most_common(N)
def topN(S, N):
    tokens = word_tokenize(S)

    clean_tokens = [token.lower() for token in tokens if token.isalpha()]

    text = nltk.Text(clean_tokens)
    vocab = text.vocab()

    return vocab.most_common(N)


sentence = "Cat cat CAT, dog dog! bird."
print(topN(sentence, 3))

sentence = "cat dog cat bird dog cat fish bird cat"
print(topN(sentence, 3))
