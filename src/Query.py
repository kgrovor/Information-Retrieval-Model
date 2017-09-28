
# coding: utf-8


import Data_Work as dw
from math import *

print(dw.newsgroups_train.target.shape)

def newquery(query):
    """Returns top 10 matching document indexes in a list to the query."""
    proc_query = dw.basic(query)
    print(proc_query)
    if(len(proc_query[0])==0):
        return [0,1,2,3,4,5,6,7,8,9]

    qtdm = {}
    for i in proc_query[0]:
        if i not in qtdm:
            qtdm[i]= dw.defaultlist([0])
            qtdm[i] = 1
    
        else:
                qtdm[i] = qtdm[i] + 1
    #print(qtdm)
    

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
            if(sq==0):
                return [0,1,2,3,4,5,6,7,8,9]
            
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
    
#==============================================================================
#     Stores all Cosine Similarities in scores. Uses Heap to avoid sorting overhead to get top 10
#==============================================================================
    import heapq
    scores = []
 
    for ech in dw.docs_vect:
        med_sum = 0
        ech_val = np.array(list(ech.values()))
        doc_norm = sqrt(np.sum(ech_val**2))
        b = doc_norm * query_norm
        if(b==0):
            b=1
        for i in query_vect[0]:
            if i in ech:
                a = ech[i]*query_vect[0][i]
            else:
                a = 0
            med_sum = med_sum + a
        scores.append(med_sum/b)
    
    scores = np.array(scores)
    #print(scores)                      
    ans = heapq.nlargest(10, range(len(scores)), scores.take)#https://stackoverflow.com/questions/6910641/how-to-get-indices-of-n-maximum-values-in-a-numpy-array
    
    print(ans,"|")
    
    return ans
  



