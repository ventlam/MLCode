#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import time
import numpy as np
import pylab as pl

from sklearn import metrics
from sklearn.cluster import k_means_
from sklearn.datasets import load_digits
from sklearn.decomposition import pca
from sklearn.preprocessing import scale

np.random.seed(8964)
#尼玛，我怎么没见这数据
digits = load_digits()
data = scale(digits)

n_sample,n_features = data.shape
n_digits = len(np.unique(digits.target))
labels = digits.target

samplesize = 300

print("n_digits: %d, \t n_samples %d, \t n_features %d"
      % (n_digits, n_samples, n_features))
