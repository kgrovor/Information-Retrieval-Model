
# coding: utf-8

# In[ ]:

import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import numpy as np
from nltk.stem import PorterStemmer
#import time
#nltk.download()
#start = time.time()
from sklearn.datasets import fetch_20newsgroups
cats = ['sci.crypt','sci.electronics','sci.med','sci.space','alt.atheism','talk.politics.guns','rec.autos','comp.windows.x','misc.forsale']
#cats = ['sci.crypt']
newsgroups_train = fetch_20newsgroups(subset='train', categories=cats)

f = open('../opinion_lexicon/positive-words.txt', 'r')
x = f.read().splitlines()

positive_words = [PorterStemmer().stem(i) for i in x]
positive_words = set(positive_words)

f2 = open('../opinion_lexicon/negative-words.txt', 'r')
x = f2.read().splitlines()

negative_words = [PorterStemmer().stem(i) for i in x]
negative_words = set(negative_words)
#print(newsgroups_train.data)

#data = ["Gambhir, +-----------------------------------+ who describes herself on Twitter as an Indian diplomat and a Delhiite, is quite familiar with Pakistan, having worked with the Pakistan division in the ministry of external affairs before being posted in New York.","At least six Pakistani villagers were killed and 26 were wounded in an overnight attack by India in the disputed Himalayan region of Kashmir, Pakistan’s military said Friday, adding that hundreds of villagers were forced to move to safer places."]
data = newsgroups_train.data
def basic(data):
    """Tokenize and Stem input data"""
    proc_data = []
    stop_words = set(stopwords.words('english'))
    stop_words.update(['.','--','+','>','-+' ,',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','>'])
    for doc in data:
        proc_data.append([i.lower() for i in (PorterStemmer().stem(x) for x in word_tokenize(doc)) if i.lower() not in stop_words])
    return proc_data

    
data = basic(data)

#==============================================================================
# Calculate Sentiment of every Document
#==============================================================================
sentiment = []
for i in data:
    sdata = set(i)
    sentiment.append(len(sdata - positive_words) - len(sdata - negative_words))  #Higher it is, the more negative the sentiment

    


class defaultlist(list):
    """If list item index is greater than list size ,appends zeroes"""
    def __setitem__(self, index, value):
      size = len(self)
      if index >= size:
         self.extend(0 for _ in range(size, index + 1))

      list.__setitem__(self, index, value)
    
tdm = {}
def make_tdm(data,tdm): 
    """Returns DataStructure of key:[Accurance in doc[i].....]"""
    for docid in range(len(data)):
        for i in data[docid]:

            if i not in tdm:
                tdm[i]= defaultlist([0])
                tdm[i][docid] = 1

            else:
                    if(docid > len(tdm[i])-1):
                        tdm[i][docid] = 1
                    else:
                        tdm[i][docid] = tdm[i][docid] + 1
    for ech in tdm:
        if len(tdm[ech]) < len(data):
            tdm[ech][len(data)-1]=0
    return tdm
tdm = make_tdm(data,tdm)

from math import *

idfs = {}
def tfidf(tdm):
    """Makes a Vector of each document and returns a list of docs"""
    docs_vect = []
    vals = list(tdm.values())
    for docid in range(len(data)):
        vectmap = {}
        vectmap.clear()
        sq = 0
        for a in vals:
            sq = sq + (a[docid] * a[docid])
        sq = sqrt(sq)
        for word in data[docid]:
            tf = tdm[word][docid]/sq
            if word in idfs:
                idf = idfs[word]
            else:
                idf = log(len(data)/np.count_nonzero(tdm[word]),10)
                idfs[word] = idf
            tfidf = tf * idf
            vectmap[word] = tfidf
        docs_vect.append(vectmap)
    return docs_vect
docs_vect = tfidf(tdm)

#print(start-time.time())       



