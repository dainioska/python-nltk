import os
import nltk
import nltk.corpus

#nltk.download()
#nltk.download("gutenberg")

from nltk.corpus import brown
#print(brown.words())
#print(nltk.corpus.gutenberg.fileids())

hamlet = nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
print(hamlet)
for word in hamlet[:500]:
    print(word, sep=' ', end=' ')

from nltk.tokenize import word_tokenize
w = """ another world is another read NLTK"""
w_t = word_tokenize(w)
print(w_t)