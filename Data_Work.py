
# coding: utf-8

# In[1]:

import nltk
from nltk import word_tokenize
import numpy as np
#nltk.download()


# In[3]:

class defaultlist(list):

   def __setitem__(self, index, value):
      size = len(self)
      if index >= size:
         self.extend(0 for _ in range(size, index + 1))

      list.__setitem__(self, index, value)
    


# In[85]:

data = ["We are implementing tf idf"," the the the the implementing"]
        
        
tdm = {}
for docid in range(len(data)):
    for i in word_tokenize(data[docid]):
        
        if i not in tdm:
            tdm[i]= defaultlist([0])
            tdm[i][docid] = 1
        
        else:
                if(docid > len(tdm[i])-1):
                    tdm[i][docid] = 1
                else:
                    tdm[i][docid] = tdm[i][docid] + 1

print(tdm)


# In[86]:

max_len = 0
ln = 0
for ech in tdm:
    ln = len(tdm[ech])
    #print(tdm[ech], " ", len(tdm[ech]))
    if(ln >= max_len):
        max_len = ln
#print(max_len) 

for ech in tdm:
    if len(tdm[ech]) < max_len:
        tdm[ech][max_len-1]=0
        
        
print(tdm)


# In[87]:

from math import *
docs_vect = []
vals = list(tdm.values())
for docid in range(len(data)):
    vectmap = {}
    vectmap.clear()
    sq = 0
    for a in vals:
        #print(a)
        sq = sq + (a[docid] * a[docid])
        #print(a[docid], " a ")
    #print(sq, "aa")
    sq = sqrt(sq)
    #print(sq , " |")
    for word in word_tokenize(data[docid]):
        tf = tdm[word][docid]/sq
        #print(tf)
        idf = log(len(data)/np.count_nonzero(tdm[word]),10)
        #print("idf = ", idf)
        tfidf = tf * idf
        vectmap[word] = tfidf
    docs_vect.append(vectmap)
    
print(docs_vect)
        


# In[58]:

vals = list(tdm.values())
print(vals)

