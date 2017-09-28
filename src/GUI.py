#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Query
from tkinter import *
import time


def printResult(searchResult,start):
    """Clears Previous results and Displays new results"""
    j = 0
    global resultsFrame
    global text
    text.delete("1.0",END)
    end = time.time()
    text.insert(END,str("Search took " + str(end-start) + " seconds\n"))
    for i in searchResult:
        j = j + 1
        if(Query.dw.sentiment[i]>0):
            sent = "(Negative Sentiment)"
        else:
            sent = "(Positive Sentiment)"
        abbr = 'Result: ' + str(j) + ' ' + sent + '\n\n'
        text.insert(END,str(abbr + Query.dw.newsgroups_train.data[i] + '\n--------------------------------------------------------------------------------------------------------------------\n'))
    text.pack(side=TOP) 
    
def printascResult(searchResult,start):
    j = 0
    global resultsFrame
    global text
    text.delete("1.0",END)
    ordered = searchResult
    ordered.sort(key = lambda x: Query.dw.sentiment[x])
    
    end = time.time()
    text.insert(END,str("Search took " + str(end-start) + " seconds\n"))
    for i in ordered:
        j = j + 1
        if(Query.dw.sentiment[i]>0):
            sent = "(Negative Sentiment)"
        else:
            sent = "(Positive Sentiment)"
        abbr = 'Result: ' + str(j) + ' ' + sent + '\n\n'
        text.insert(END,str(abbr + Query.dw.newsgroups_train.data[i] + '\n--------------------------------------------------------------------------------------------------------------------\n'))
    text.pack(side=TOP) 
    
def printdescResult(searchResult,start):
    j = 0
    global resultsFrame
    global text
    text.delete("1.0",END)
    ordered = searchResult
    ordered.sort(key= lambda x: Query.dw.sentiment[x], reverse=True)
    end = time.time()
    text.insert(END,str("Search took " + str(end-start) + " seconds\n"))
    for i in ordered:
        j = j + 1
        if(Query.dw.sentiment[i]>0):
            sent = "(Negative Sentiment)"
        else:
            sent = "(Positive Sentiment)"
        abbr = 'Result: ' + str(j) + ' ' + sent + '\n\n'
        text.insert(END,str(abbr + Query.dw.newsgroups_train.data[i] + '\n--------------------------------------------------------------------------------------------------------------------\n'))
    text.pack(side=TOP) 

def fns():
    """Calls print on GUI"""
    a = e1.get()
   
    start = time.time()
    printResult(Query.newquery([a]),start)

def fns1():
    a = e1.get()
    start = time.time()
    printascResult(Query.newquery([a]),start)
    
def fns2():
    a = e1.get()
    start = time.time()
    printdescResult(Query.newquery([a]),start)
    
#==============================================================================
# Builds the on screen GUI
#==============================================================================

root = Tk()

topFrame = Frame(root)
topFrame.pack(side = TOP)

root.wm_title("Vector Space Model")
root.minsize(width=1000, height=900)

intro = Label(topFrame,text="IR ASSIGNMENT 1\n Email Search",bg="grey",fg="black")
intro.pack(fill=X)

Label(topFrame, text="Query").pack(side = LEFT)
e1 = Entry(topFrame)
e1.pack(side = RIGHT)



bottomFrame = Frame(root)
bottomFrame.pack(side=TOP)
searchButton = Button(bottomFrame,text='Search!', command=fns)
searchButton.pack(side = TOP)

 
sentiA = Button(bottomFrame,text='Positive First', command=fns1)
sentiA.pack(side = RIGHT)
sentiB = Button(bottomFrame,text='Negative First', command=fns2)
sentiB.pack(side = RIGHT)





resultsFrame = Frame(root)
resultsFrame.pack(side=TOP)
text = Text(resultsFrame, height=888, width=888, bg="black")

root.mainloop()