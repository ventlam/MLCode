#!/usr/bin/env python
# -*- coding: utf-8 -*-
from numpy import *
#
def loadDataSet():
    postList = [['my','dog','has','flea'],
                ['shit','fuck','dog','damn','you'],
                ['so','cute','my','dog','love','him'],
                ['mr','lick','my','ass','dummy']]
    classVec = [0,1,0,1]
    return postList,classVec
#创建语料库
def creatVocabList(dataSet):
    vocabSet = set([]) #Set (无序,无重复元素),以数组作为元素？
    for doc in dataSet:
        vocabSet = vocabSet | set(doc) #求并集
    return list(vocabSet)
#判断语料库的单词是否出现在输入文档，返回词向量
def setWord2Vec(vocabList,inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "word: %s is not in our vocabulary" % word
    print returnVec
    return returnVec
#navie bayes training
#输入文档矩阵，每篇文档类别标签所构成的向量
def trainNavieBayes(trainMaxtrix,trainCategory):
    numTrainDocs = len(trainMaxtrix) #训练文档大小?
    numWords = len(trainMaxtrix[0]) #？
    #the items of an iterable from left to right and returns the total.
    pAbsuvie = sum(trainCategory) / float(numTrainDocs)
    poNum = zeros(numWords) #np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
    p1Num = zeros(numwords) #Return a new array of given shape and type, filled with zeros.
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMaxtrix[i]
            p1Denom += sum(trainMaxtrix[i]) #?
        else:
            p0Num += trainMatrix[i]
            p9Denom += sum(trainMaxtrix[i])
    p0vect = p0Num / p0Denom
    p1vect = p1Num / p1Denom
    print p1vect,p0vect
    return p0vect,p1vect,pAbsuvie

#主函数这种东西，我也不知道为什么应该存在
def main():
    postlist,clavec = loadDataSet()
    vocabList = creatVocabList(postlist)
    #wordlist = ['abs','my']
    setWord2Vec(vocabList,postlist[0])

main()
