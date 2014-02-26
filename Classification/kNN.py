from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def classify(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0] #数据集大小
    diffMat = tile(inX,(dataSetSize,1)) - dataSetSize
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis=1) #???


