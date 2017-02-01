# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 22:42:10 2016

@author: Jialiang Yu
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math
import string



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
for i in range((len(character))) :
    A[character[i]-1][book[i]-1] = 1
print A[0][0]


"""
x = xrange(0,100)
y = np.zeros(len(x))
z = ["aa","bb","cc"]
d = [10,9,9,9,9,7,7,6,4,2,1]

for i in range(len(d)-1) :
    print d[i+1]

m = 0
cc = []

for i in range(len(d)) :
    
    
        if d[i] != d[i-1] :
            m = i
            cc.append(i)
        else :
            cc.append(m)
print cc 

"""

"""
a = open("E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\Marvel-data\CB.txt", "r")  
b = a.readlines()
print (len(b))
print (b)

"""

"""

dic = {}
fp=open("E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\Marvel-data\marvel.txt")

for linea in fp.readlines():
    character = linea.split(" ")[:-1]
    book = linea.split(" ")[1:]
"""     
"""
    if character in dic :
        dic[character].append(book)
    else :
        dic[character] = []
        character.append(book)
    
print character,book    
    
fp.close()
#print result
print dic
"""






"""

result2 = [j for i in result for j in i]
print result2

"""
"""
haha = []
for item in result2 :
    haha.append(item.strip())
print haha
"""













"""
#make a dictionary
dic = {}
for i in range(len(character)) :
    if dic.has_key(character[i]) :
        dic[character[i]].append(book[i])
    else :
        dic.update({character[i]:[book[i]]})
print dic
"""

"""

adjacency = [[] for i in range(6486)]  #建立6486个list

"""

"""
add = np.zeros((12942,), dtype=np.int)

for number in dic[1] :
    add[number-6487] = 1
print sum(add)
"""


"""
for i in range(12942) :
    for key in dic :

            for number in dic[key] :
                add[number-6487] = 1
                adjacency.append(add)
            add = np.zeros((12942,), dtype=np.int)
print adjacency   
"""

"""
i = 0
index = 0

for key in dic:
    for number in dic[key] :
        while(index < 12942) :
            if index == number :
                adjacency[i].append(1)
            else :
                adjacency[i].append(0)
            index += 1
        i += 1

print adjacency




 
for 
"""






















"""

character = []
book = []
for item in r2 :
    character.append(string.atoi(item))
for item in haha :
    book.append(string.atoi(item))
    
print character
print book
#print len(character), len(book)


"""

    



























