# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 13:53:16 2016

@author: Jialiang Yu
"""
import csv
import numpy as np


            
#creat empty matrix
A = [[0 for col in range(10312)] for row in range(10312)]
B = [[-1 for col in range(10312)] for row in range(10312)]

#read data
reader=csv.reader(open("E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\Midterm\edges\edges.csv","rb"),delimiter=',')
#transfer to list
data=list(reader)
#construct adjacency matrix
for item in data :
    a = int(item[0]) -1
    b = int(item[1]) -1
    A[a][b] = 1
#initialization
a = []
summary = 0
N = 10312

#prediction with Jaccard Similarity
for i in range(N):
    for j in range(N):
        summary += A[i][j]
    if summary > 10:
        a.append(i)
        summary = 0
for i in range(len(a)):
    for j in range(N):
        if A[a[i]][j] == 0 and a[i]!=j :
            intersection = 0
            cup = 0
            for y in range(N):
                if A[a[i]][y] == 1 and A[j][y] == 1:
                    intersection += 1
                elif A[a[i]][y] + A[j][y] != 0:
                    cup += 1
                else:
                    continue
            B[a[i]][j] = float(intersection)/cup
            
C = []
count = 0
for i in range(N):
    while(count<5):
        index = np.argmax(B[i])
        C.append([i,index])
        B[i][index] = -1
        count += 1
    count = 0    
           
        
#write result to file
ar = np.asarray(C)
fl = open('E:/Purdue Courses/Second semester/CS573 Data Mining/CS573 homework/Midterm/edges/result.csv','wb')
writer = csv.writer(fl)
for values in ar:
    writer.writerow(values)
fl.close()









