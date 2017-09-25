
# coding: utf-8

# In[2]:
import nltk
from nltk import word_tokenize
from nltk.stem import PorterStemmer

f = open('opinion_lexicon/positive-words.txt', 'r')
x = f.read().splitlines()

positive_words = [PorterStemmer().stem(i) for i in x]
positive_words = set(positive_words)

f2 = open('opinion_lexicon/negative-words.txt', 'r')
x = f2.read().splitlines()

negative_words = [PorterStemmer().stem(i) for i in x]
negative_words = set(negative_words)
# In[ ]:



