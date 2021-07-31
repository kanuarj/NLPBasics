# Corpus ~ A collection of Texts
# Stop Words ~ Are collection of words which can be filtered out while processing the text

text = 'My name is Raunak and welcome to my NLP Series.'

from nltk.corpus import stopwords
stop_words = stopwords.words('english')

from nltk.tokenize import word_tokenize
words = word_tokenize(text)

# holder = list()
# for w in words:
#     if w not in set(stop_words):
#         holder.append(w)

# List Comprehension

holder = [w for w in words if w not in set(stop_words)]
print(holder)