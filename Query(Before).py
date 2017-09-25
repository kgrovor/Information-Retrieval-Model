
# coding: utf-8

# In[7]:

import Data_Work as dw


# In[10]:

query = ["yolo lol"]
proc_query = dw.basic(query)
print(proc_query)


# In[11]:

qtdm = {}
for i in proc_query[0]:
    if i not in qtdm:
        qtdm[i]= dw.defaultlist([0])
        qtdm[i] = 1

    else:
        if(docid > len(qtdm[i])-1):
            qtdm[i] = 1
        else:
            qtdm[i] = qtdm[i] + 1
print(qtdm)


# In[12]:

from math import *
import numpy as np
def tfidf(tdm,data):
    docs_vect = []
    vals = list(tdm.values())
    for docid in range(len(data)):
        vectmap = {}
        vectmap.clear()
        sq = 0
        for a in vals:
            sq = sq + pow(a,2)
        sq = sqrt(sq)
        for word in data[docid]:
            tf = tdm[word]/sq
            if word in dw.idfs:
                idf = dw.idfs[word]
            else:
                idf = 0
            
            tfidf = tf * idf
            vectmap[word] = tfidf
        docs_vect.append(vectmap)
    return docs_vect

query_vect = tfidf(qtdm,proc_query)
print(query_vect)


# In[ ]:



