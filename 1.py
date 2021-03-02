import nltk
import matplotlib.pyplot as plt

#nltk.download()
#nltk.download('punkt')

text = """ Welcome you to programming knowlege NLTK. Lets start with our NLTK programming"""

from nltk.tokenize import word_tokenize
word_tokenized = word_tokenize(text)
#print(word_tokenize(text))

#from nltk.tokenize import sent_tokenize
#print(sent_tokenize(text))

from nltk.probability import FreqDist
fd = FreqDist(word_tokenized)
print(fd.most_common(3))
fd.plot(30,cumulative=False)
plt.show()






