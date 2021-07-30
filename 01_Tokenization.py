# Tokenization

# import nltk
# nltk.download()

# 1. Sentence Tokenization

from nltk.tokenize import sent_tokenize

text = 'My name is Raunak and welcome to my YouTube channel. Subscribe if you like.'

sentences = sent_tokenize(text)
# print(sentences)

# 2. Words Tokenization

from nltk.tokenize import word_tokenize

words = word_tokenize(text)

# for w in words:
#     print(w)