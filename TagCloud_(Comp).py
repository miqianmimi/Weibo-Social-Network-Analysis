# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 14:32:02 2017

@author: Air
"""

import jieba
import jieba.posseg as pseg
import os
import string
import sys
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import sys
from numpy import *
import string

def removeblank():
    input = open('1.txt')
    output = open('1remove.txt', 'w')
    info = input.read()
    pp = ''
    for tt in info.splitlines():
        tt=tt.rstrip()
        pp=pp+tt
    output.write(pp)
    input.close()
    output.close()

removeblank()
    
    
fr=open('1remove.txt')
fr_list=fr.read()

dataList=fr_list.split('\n')
#dataList=fr.readline().rstrip()
print dataList
#print fr_list

#data=[]
#直接分词
#for oneline in dataList:
 #   print oneline
 #   data.append(" ".join(jieba.cut(oneline))) 
#print data
#去英文
data1 = []
for oneline in dataList:
    print oneline
    data1.append(''.join([x for x in oneline if not x.isalpha()]))
#print data1
#去数字
data2=[]
for oneline in data1:
    data2.append(''.join([x for x in oneline if not x.isdigit()]))
#print data2
#分词
data3=[]
for oneline2 in data2:
    #print oneline2
    data3.append(" ".join(jieba.cut(oneline2)))
#print data3

fr.close()


freWord = CountVectorizer()
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(freWord.fit_transform(data3))
word = freWord.get_feature_names()
#print word
#打印词数并且计数
#a=0
for i in word:
    print i
#    a=a+1
#print a
weight = tfidf.toarray()
#print weight
#print size(weight)
#print weight[100]
tfidfDict = {}
for i in range(len(weight)):
    for j in range(len(word)):
        getWord = word[j]
        getValue = weight[i][j]
        if getValue != 0:
            if tfidfDict.has_key(getWord):
                tfidfDict[getWord] +=string.atof(getValue)
            else:
                tfidfDict.update({getWord:getValue})
sorted_tfidf = sorted(tfidfDict.iteritems(),
                      key = lambda d:d[1],reverse =True)
fw = open('result2.txt','w')
for i in sorted_tfidf:
    #print i[0].encode('utf-8')
    #print i[1]
    fw.write("Word: %s " %i[0].encode('utf-8'))
    fw.write(" ")
    fw.write("TF-IDF: %s" %i[1])
    fw.write("\r\n")
    
fw.close()

fw1 = open('result3.txt','w')
for i in sorted_tfidf:
    print i[0].encode('utf-8')
    print i[1]
    fw1.write("%s" %i[0].encode('utf-8'))
    fw1.write("\r\n")
    
fw1.close()