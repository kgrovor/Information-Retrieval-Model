
# coding: utf-8

# In[2]:

import Data_Work as dw
from math import *

# In[13]:

print(dw.newsgroups_train.target.shape)

def newquery(query):
    proc_query = dw.basic(query)
    print(proc_query)
    
    
    # In[14]:
    
    qtdm = {}
    for i in proc_query[0]:
        if i not in qtdm:
            qtdm[i]= dw.defaultlist([0])
            qtdm[i] = 1
    
        else:
                qtdm[i] = qtdm[i] + 1
    print(qtdm)
    
    
    # In[15]:
    
    
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
    qlist = np.array(list(query_vect[0].values()))
    query_norm = sqrt(np.sum(qlist**2))
    
    
    # In[16]:
    
    import heapq
    scores = []
    for ech in dw.docs_vect:
        med_sum = 0
        ech_val = np.array(list(ech.values()))
        doc_norm = sqrt(np.sum(ech_val**2))
        b = doc_norm * query_norm
        for i in query_vect[0]:
            if i in ech:
                a = ech[i]*query_vect[0][i]
            else:
                a = 0
            med_sum = med_sum + a
        scores.append(med_sum/b)
    
    scores = np.array(scores)
    #print(scores)
    ans = heapq.nlargest(10, range(len(scores)), scores.take)
    print(ans)
    
    
    # In[17]:
    
    for i in ans:
        print(dw.newsgroups_train.data[i])
    
    
for i in range(4):
    a = input("Enter Query:")
    newquery([a])




