# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 22:23:22 2016

@author: Jialiang Yu
"""

from __future__ import division
import string

from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import math


character=[]
book=[]

fp=open("E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\Marvel-data\marvel.txt")
r=[]
for linea in fp.readlines():
    linea=linea.split(" ")[:-1]
    r.append(linea)
fp.close()

r2 = [j for i in r for j in i]



fp=open("E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\Marvel-data\marvel.txt")
b=[]
for linea in fp.readlines():
    linea = linea.strip('\n')
    linea=linea.split(" ")[1:]
    b.append(linea)
fp.close()

b2 = [j for i in b for j in i]



for item in r2 :
    character.append(string.atoi(item))
for item in b2 :
    book.append(string.atoi(item))



A = [[0 for x in range(19428)] for x in range(6486)] 
for i in range(len(character)) :
    A[character[i]-1][book[i]-1] = 1

AT = [list(i) for i in zip(*A)]

"""
k = [[0 for x in range(6486)] for x in range(6486)]
for i in range(6486) :
    for j in range(19428) :
        k[i][i] += A[i][j] * A[i][j]
"""
"""
kk = np.matrix(k)
kkk = kk.max()

for ha in range(6486) :
    if k[i][i] == kkk:
        print ha
        break
"""

A_mat = np.matrix(A)
AT_mat = np.matrix(AT)
W = A_mat * AT_mat














