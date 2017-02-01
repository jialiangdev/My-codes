# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:35:59 2016

@author: Jialiang Yu
"""

import math
import csv
import numpy
import random
import matplotlib.pyplot as plt
import pandas as pd
from itertools import islice

"""
n_arm = 4
#e-greedy  第一问

reward = [0,1,1,0]
count = [1,1,1,1]
best_list = [0.0 for i in range(n_arm)]


def my_choice(epsilon):
    rand = random.uniform(0,1)
    if rand > epsilon:
        n = choose_best(n_arm)
    else:
        n = random.randint(0,3)
    return n


def ind_max(x):
    m = max(x)
    return x.index(m)


def choose_best(n_arm):
    for i in range(n_arm):
        best_list[i] = float(reward[i])/count[i]
    return ind_max(best_list)


reader=csv.reader(open("E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\dd.csv","rb"),delimiter=',')
x=list(reader)
arm = numpy.array(x).astype('float')

total = 4
epsilon = 0.8
arm_a = [1,1,1,1]
arm_b = [0,1,1,1]
arm_c = [0,0,1,1]
arm_d = [0,0,0,1]

while(total<1000):
    n = my_choice(n_arm)   
    count[n] += 1
    total += 1
    m = total
    reward[n] += arm[m-1][n]
    arm_a.append(count[0])
    arm_b.append(count[1])
    arm_c.append(count[2])
    arm_d.append(count[3])    
    
    
print count
print reward


print sum(count)
print sum(reward)

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
plt.savefig('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\egreedy_1.png',dpi=1000)
plt.show()
"""









n_arm = 4

#e-greedy  第一问

reward = [0,1,1,0]
count = [1,1,1,1]
best_list = [0.0 for i in range(n_arm)]


def my_choice(epsilon):
    rand = random.uniform(0,1)
    if rand > epsilon:
        n = choose_best(n_arm)
    else:
        n = random.randint(0,3)
    return n


def ind_max(x):
    m = max(x)
    return x.index(m)


def choose_best(n_arm):
    for i in range(n_arm):
        best_list[i] = float(reward[i])/count[i]
    return ind_max(best_list)




def getDonaList(filename):
    DonaList=[]
    with open(filename) as file:
        file.next();
        for eachline in file:
            ID, donation = eachline.strip().split(',')
            DonaList.append(float(donation))
    return DonaList

DonaList1b = getDonaList('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population1b.csv')
DonaList2b = getDonaList('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population2b.csv')
DonaList3b = getDonaList('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population3b.csv')
DonaList4b = getDonaList('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population4b.csv')
DonaList1p = getDonaList('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population1p.csv')
DonaList2p = getDonaList('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population2p.csv')
DonaList3p = getDonaList('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population3p.csv')
DonaList4p = getDonaList('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population4p.csv')

arm_original = [DonaList1p, DonaList2p, DonaList3p, DonaList4p]
arm_s = map(list, zip(*arm_original))
arm = [[0.0 for col in range(4)] for row in range(1000)]
for i in range(1000) :
    for j in range(4) :
        arm[i][j] = float(arm_s[i][j]) / 452.94




n_arm = 4

counts = [1,1,1,1]    # how many times does an arm be played
value = [0.00282598,0.0022078,0.0022078,0.0022078]    # total value of an arm since first playing    
ucb_values = [0.0 for col in range(n_arm)]








total = 4
epsilon = 0.1
arm_a = [1,1,1,1]
arm_b = [0,1,1,1]
arm_c = [0,0,1,1]
arm_d = [0,0,0,1]

while(total<1000):
    n = my_choice(n_arm)   
    count[n] += 1
    total += 1
    m = total
    reward[n] += arm[m-1][n]
    arm_a.append(count[0])
    arm_b.append(count[1])
    arm_c.append(count[2])
    arm_d.append(count[3])    
    
    
print count
print reward
for item in reward:
    print item * 452.94


print sum(count)
print sum(reward)*452.94

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
plt.savefig('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\egreedy_2.png',dpi=1000)
plt.show()




    




"""


#UCB1  b的
#(i) 

def ind_max(x):
    m = max(x)
    return x.index(m)

n_arm = 4

counts = [1,1,1,1]    # how many times does an arm be played
value = [0,1,1,0]    # total value of an arm since first playing    
ucb_values = [0.0 for col in range(n_arm)]

def choose(n_arm) :    
    
    for i in range(n_arm) :
        ucb_values[i] = float(value[i])/counts[i] + math.sqrt(2 * math.log(sum(counts))/counts[i])
    
    return ind_max(ucb_values)


reader=csv.reader(open("E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\dd.csv","rb"),delimiter=',')
x=list(reader)
arm = numpy.array(x).astype('float')

total = 4



arm_a = [1,1,1,1]
arm_b = [0,1,1,1]
arm_c = [0,0,1,1]
arm_d = [0,0,0,1]

while(total<1000):
    n = choose(n_arm)   
    counts[n] += 1
    total += 1
    m = total
    value[n] += arm[m-1][n]
    arm_a.append(counts[0])
    arm_b.append(counts[1])
    arm_c.append(counts[2])
    arm_d.append(counts[3])    
    
    
print counts
print value
print ucb_values

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
plt.savefig('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\ubc_b.png',dpi=1000)
plt.show()

"""







"""

#UCB1  p的
#(ii)


def getDonaList(filename):
    DonaList=[]
    with open(filename) as file:
        file.next();
        for eachline in file:
            ID, donation = eachline.strip().split(',')
            DonaList.append(float(donation))
    return DonaList

DonaList1b = getDonaList('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population1b.csv')
DonaList2b = getDonaList('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population2b.csv')
DonaList3b = getDonaList('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population3b.csv')
DonaList4b = getDonaList('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population4b.csv')
DonaList1p = getDonaList('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population1p.csv')
DonaList2p = getDonaList('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population2p.csv')
DonaList3p = getDonaList('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population3p.csv')
DonaList4p = getDonaList('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population4p.csv')

arm_original = [DonaList1p, DonaList2p, DonaList3p, DonaList4p]
arm_s = map(list, zip(*arm_original))
arm = [[0.0 for col in range(4)] for row in range(1000)]
for i in range(1000) :
    for j in range(4) :
        arm[i][j] = float(arm_s[i][j]) / 452.94


def ind_max(x):
    m = max(x)
    return x.index(m)

n_arm = 4

counts = [1,1,1,1]    # how many times does an arm be played
value = [0.00282598,0.0022078,0.0022078,0.0022078]    # total value of an arm since first playing    
ucb_values = [0.0 for col in range(n_arm)]

def choose(n_arm) :    
    
    for i in range(n_arm) :
        ucb_values[i] = float(value[i])/counts[i] + math.sqrt(2 * math.log(sum(counts))/counts[i])
    
    return ind_max(ucb_values)




total = 4

arm_a = [1,1,1,1]
arm_b = [0,1,1,1]
arm_c = [0,0,1,1]
arm_d = [0,0,0,1]

while(total<1000):
    n = choose(n_arm)   
    counts[n] += 1
    total += 1
    m = total
    value[n] += arm[m-1][n]
    arm_a.append(counts[0])
    arm_b.append(counts[1])
    arm_c.append(counts[2])
    arm_d.append(counts[3])    
    
    
print counts
print value
#print ucb_values

for item in value:
    print 452.94 * item



print sum(counts)
print 452.94 * sum(value)

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
plt.savefig('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\ubc_p.png',dpi=1000)
plt.show()


"""



















