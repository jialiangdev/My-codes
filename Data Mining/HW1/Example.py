# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:38:36 2016

@author: Jialiang Yu
"""


import numpy as np
from matplotlib import use
import math
use('Agg')
import matplotlib.pyplot as plt


fp=open("E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\Marvel-data\marvel.txt")
result=[]
for linea in fp.readlines():
    linea=linea.split(" ")[:-1]
    result.append(linea)
fp.close()
#print result
result2 = [j for i in result for j in i]
print result2


from collections import Counter
count = Counter(result2) 
#c = list(count)
print count
print len(count)


c = []
for key in count :
    c.append(count[key])
print c

d = sorted(c,reverse = True)
print d
print len(d)


m = 0
cc = []

for i in range(len(d)) :
    
    
        if d[i] != d[i-1] :
            m = i
            cc.append(i)
        else :
            cc.append(m)
print cc
print len(cc)
"""


d = cc
p = 0.8
ECCDF = 1.0
x = []
y = []

for d in cc:
	#Be careful with machine precision
	x.append(d)
	y.append(ECCDF)
	ECCDF = ECCDF - (1-p)*p**d
print(x)
print(y)
plt.xlim([1,max(x)])
plt.xlabel("node degree", fontsize=18)
plt.ylabel("ECCDF", fontsize=18)
plt.loglog(x,y,"ro")
plt.savefig('ECCDF_plot.pdf')
"""