# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 08:41:04 2016

@author: Jialiang Yu
"""
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import math



fp=open("E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\Marvel-data\marvel.txt")
result=[]
for linea in fp.readlines():
    linea=linea.split(" ")[:-1]
    result.append(linea)
fp.close()
#print result
result2 = [j for i in result for j in i]
print result2



count = Counter(result2) 
#c = list(count)
print count
print len(count)
"""
for key in count :
    print '%s : %d' % (key,count[key])

"""
"""
x = []

value = 0
fix = 1
while(fix < 1626) :
    for key in count :
        if count[key] > fix :
            value += 1
    x.append(value)
    value = 0
    fix += 1
"""


c = []
for key in count :
    c.append(count[key])
print c

d = sorted(c,reverse = True)
print d

i = 0
time = 0
dude = []
while(i < 1626) :
    for number in d :
        if number > i :
            time += 1
        else :
            time += 0
    dude.append(time)
    i += 1   
    time = 0     
print dude
print len(dude)


"""
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




y = []
for i in dude :
    y.append(float(i)/6486)
print y

x = []
k = 1626
for kk in xrange(k) :
    x.append(kk)    

plt.ylabel('ECCDF')
plt.xlabel('comic book appearances')
plt.xlim([1,max(x)])
#X, Y AXIS
plt.loglog(x,y,'bo')
#plt.plot(cc,y,'ro')
plt.legend()
plt.figure.figsize = (1024,1024)
plt.figure.dpi = 300
plt.facecolor = 0.8
plt.savefig('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\Marvel-data\final.png',dpi=1000)
plt.show()













"""

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

def implicitplot3d(fn, bbox=(-1.5,1.5)):
    xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    A = np.linspace(xmin, xmax, 50)
    B = np.linspace(xmin, xmax, 20)
    A1,A2 = np.meshgrid(A,A)
    for z in B:
        X,Y = A1,A2
        Z = fn(X,Y,z)
        cset = ax.contour(X, Y, Z+z, [z], zdir='z')
    for y in B:
        X,Z = A1,A2
        Y = fn(X,y,Z)
        cset = ax.contour(X, Y+y, Z, [y], zdir='y')
    for x in B:
        Y,Z = A1,A2
        X = fn(x,Y,Z)
        cset = ax.contour(X+x, Y, Z, [x], zdir='x')
    ax.set_zlim3d(zmin,zmax)
    ax.set_xlim3d(xmin,xmax)
    ax.set_ylim3d(ymin,ymax)
    plt.show()

implicitplot3d(lambda x,y,z: (x*x + 2*y*y + z*z -1)**3 - x*x*z*z*z - y*y*z*z*z/10.)
"""







