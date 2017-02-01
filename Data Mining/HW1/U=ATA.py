# -*- coding: utf-8 -*-


from __future__ import division
import string
import numpy as np


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

AT = map(list, zip(*A))




k = [[0 for x in range(19428)] for x in range(19428)]
for i in range(19428) :
    for j in range(6486) :
        k[i][i] += A[j][i] * A[j][i]


kk = np.matrix(k)
kkk = kk.max()


for ha in range(19428) :
    if k[ha][ha] == 111:
        print ha
        break





