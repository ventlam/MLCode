#!/usr/bin/env python
# -*- coding: utf-8 -*-
from numpy import *
from StringIO import StringIO

def processCSV():
    data =  genfromtxt('/Users/vent/github/MLCode/resource/bjhot.csv',delimiter=',')
#You can ask np.genfromtxt to try to guess the actual type of your columns by using dtype=None:
#跳过头尾N行,不显示指定数据类型
    datahf = genfromtxt('/Users/vent/github/MLCode/resource/bjhot.csv',delimiter=',',skip_header=2,skip_footer=140,dtype=None)
    print(data[:10,:2])
    print(datahf)

processCSV()
