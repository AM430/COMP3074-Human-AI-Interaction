"""Environment check only; this is not a Lab exercise solution."""

import sys

import nltk
from bs4 import BeautifulSoup

print("Python:", sys.version.split()[0])
print("Interpreter:", sys.executable)
print("Virtual environment:", sys.prefix != sys.base_prefix)
print("NLTK:", nltk.__version__)
print("Tokens:", nltk.tokenize.wordpunct_tokenize("Hello, Human-AI!"))
print("HTML text:", BeautifulSoup("<p>Hello, Human-AI!</p>", "html.parser").get_text())
