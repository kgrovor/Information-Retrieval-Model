
# coding: utf-8

# In[5]:

import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import numpy as np
from nltk.stem import PorterStemmer
#nltk.download()


# In[11]:

data = ["The iPhone 8 and 8 Plus, two of the three new iPhones in Apple’s 2017 lineup, went on sale around the world, starting in Australia where hundreds of people have usually gathered outside Apple’s Sydney city store for previous launches. But instead of queues winding down the street there were fewer than 30 people lining up before the store opened on Friday."," At first, East Central University — a public university with 4,000 students in Ada, about 80 miles (130 kilometers) southeast of Oklahoma City — complied with the request from Americans United for Separation of Church and State, removing Bibles and other Christian-themed items from the colonial-style chapel that was donated by a longtime regent in 1957. But before the cross could be taken down, the matter had drawn the attention of religious leaders as well as Oklahoma's Republican attorney general, who is running for re-election next year."]


def basic(data):
    proc_data = []
    stop_words = set(stopwords.words('english'))
    stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
    for doc in data:
        proc_data.append([i.lower() for i in (PorterStemmer().stem(x) for x in word_tokenize(doc)) if i.lower() not in stop_words])
    return proc_data

    
data = basic(data)
print(data)


# In[12]:

class defaultlist(list):

   def __setitem__(self, index, value):
      size = len(self)
      if index >= size:
         self.extend(0 for _ in range(size, index + 1))

      list.__setitem__(self, index, value)
    


# In[13]:

#data = ["We are implementing tf idf"," the the the the implementing"]
        
        
tdm = {}
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

print(tdm)


# In[16]:

for ech in tdm:
    if len(tdm[ech]) < len(data):
        tdm[ech][len(data)-1]=0
        
print(tdm)


# In[18]:

from math import *
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
        idf = log(len(data)/np.count_nonzero(tdm[word]),10)
        tfidf = tf * idf
        vectmap[word] = tfidf
    docs_vect.append(vectmap)
    
print(docs_vect)
        


# In[ ]:



