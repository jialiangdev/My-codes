# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 21:12:22 2016

@author: Jialiang Yu
"""
import math
import csv
import numpy
import random
import matplotlib.pyplot as plt
import pandas as pd
from itertools import islice
from scipy.stats import beta

def ind_max(x):
    m = max(x)
    return x.index(m)

def choose(n_arm,mean_list,S,F) :    

    
    for i in range(n_arm):
        mean = beta.rvs(S[i]+0.01, F[i]+0.01, size=1)  
        mean_list[i] = mean       
    n = ind_max(mean_list)
    return n



reader=csv.reader(open("E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\dd.csv","rb"),delimiter=',')
x=list(reader)
arm = numpy.array(x).astype('float')

n_arm = 4

counts = [1,1,1,1]    # how many times does an arm be played
value = [0,1,1,0]    # total value of an arm since first playing 
S=[0,1,1,0]
F=[1,0,0,1]
mean_list = [0,0,0,0]
total = 4

arm_a = [1,1,1,1]
arm_b = [0,1,1,1]
arm_c = [0,0,1,1]
arm_d = [0,0,0,1]

while(total<1000):
    n = choose(n_arm,mean_list,S,F)
    counts[n] += 1
    total += 1
    m = total
    if arm[m-1][n] == 1:
        S[n] += 1
    else:
        F[n] += 1
   
    value[n] += arm[m-1][n]
    arm_a.append(counts[0])
    arm_b.append(counts[1])
    arm_c.append(counts[2])
    arm_d.append(counts[3])    
    
    
print counts
print value
print total

print sum(counts)
print sum(value)




t = numpy.arange(0., 1000., 1.)
plt.ylabel('Cumulative times of each arm')
plt.xlabel('total time of pull')

plt.figure.figsize = (1024,1024)

# red dashes, blue squares and green triangles
plt.plot(t, arm_a, 'r', label = 'Arm_1')
plt.plot(t, arm_b, 'b', label = 'Arm_2')
plt.plot(t, arm_c, 'g', label = 'Arm_3')
plt.plot(t, arm_d, 'y', label = 'Arm_4')

plt.grid()
plt.legend(loc=2)
plt.savefig('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\kaka4.png',dpi=1000)
plt.show()
        



