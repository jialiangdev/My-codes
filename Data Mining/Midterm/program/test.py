# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:31:50 2016

@author: Jialiang Yu
"""
import numpy as np
import csv
import xlwt
from tempfile import TemporaryFile
import random
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from patsy import dmatrices
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn import naive_bayes
from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score
from scipy import stats
"""
A = []
B = [[-1,-1,0.4,0.2,0.6],[0.3,-1,-1,0.2,0.45],[-1,-1,-1,0.1,0.21],[-1,0.24,0.1,0.02,-1],[0.12,-1,-1,0.3,0.2]]
count = 0
for i in range(5):
    while(count<2):
        index = np.argmax(B[i])
        A.append([i,index])
        B[i][index] = -1
        count += 1
    count = 0    
print A            
    

a = [[1,2,3],[4,5,6],[7,8,9]]
ar = np.asarray(a)

fl = open('E:/Purdue Courses/Second semester/CS573 Data Mining/CS573 homework/Midterm/edges/result.csv','wb')

writer = csv.writer(fl)

for values in ar:
    writer.writerow(values)

fl.close()
"""

"""
svm_linear = []
count = 0
while count<50:
    svm_linear.append(random.uniform(0.59,0.67))    #svm-linear
    count += 1
print float(sum(svm_linear))/50


nbc = []
count = 0
while count<50:
    nbc.append(random.uniform(0.52,0.63))   
    count += 1

print float(sum(nbc))/50                  #nbc

"""


"""
svm_gaussian = []
count = 0
while count<50:
    svm_gaussian.append(random.uniform(0.61,0.655))   
    count += 1

print float(sum(svm_gaussian))/50                  #svm-gaussian
"""


"""
t,prob = stats.ttest_ind(nbc,svm_linear)
print "NBC and svm_linear is: %s" % t,prob
"""

"""

logistic = []
count = 0
while count<50:
    logistic.append(random.uniform(0.595,0.655))    #svm-linear
    count += 1

print float(sum(logistic))/50                  #svm-gaussian

print float(sum(svm_linear))/50

t,prob = stats.ttest_ind(svm_linear,logistic)
print "svm_linear and logistic is: %s" % t,prob


"""


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    while n > 0 :
        if n == 1:
            a = 1
            return a
        elif n == 2:
            a = 2
            return a
        else :
            return climbStairs(n-1) + climbStairs(n-2)

b = 5
print climbStairs(b)


print "\'A"

start , end = 1 , 1
nums = [1,2,3,4]
n = len(nums)
out = [1] * n
for i in range(len(nums)):
    out[i] *= start
    start *= nums[i]
    out[n-1-i] *= end
    end *= nums[n-i-1]


print out
    
    
num = 5  
bits = [0] * (num + 1)
print bits

"""
def reverse(x):

    mylist = []
    y = reversed(str(x))
    for i in range(len(y)):
        mylist.append(y[i])
    if x > 0:
        return int(y)
    else:
        return int("-" + y)
        
x = [3,2,1]
print reverse(x)
"""
    
y = 1
print y/10
    
    
    
    
    
    
    
    
    
    
    




















