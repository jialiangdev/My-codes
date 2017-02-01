# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 08:57:38 2016

@author: Jialiang Yu
"""
import csv
import numpy as np

matrix = []
A = [[0 for i in range(40)] for j in range(1000)]


reader=csv.reader(open("E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW3\mystery_data.txt","rb"),delimiter=',')
data=list(reader)
for lst in data:
    mylist = []
    for i in range(len(lst)):
        mylist.append(float(lst[i]))
    matrix.append(mylist)

for i in range(40000):
    A[int(matrix[i][0])][int(matrix[i][1])] = matrix[i][2]

U,s,V = np.linalg.svd(A) # SVD decomposition 

print np.shape(U)
print np.shape(s)
print np.shape(V)
print np.shape(A)

B = np.dot(U,np.diag(s)).dot(V)
print B.shape()