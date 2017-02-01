# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 21:28:38 2016

@author: Jialiang Yu
"""
"""
import xlrd

def average(data) :
    table = data.sheet()[0]
    total = 0
    nrows = table.nrows
    for i in range(nrows) :
        total += table.col(1)[i].value
    average = float(total/nrows)
    return average
    
data1 = xlrd.open_workbook('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population1b.csv')
data2 = xlrd.open_workbook('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population2b.csv')

print average(data1)
print average(data2)
"""

import csv
from scipy import stats

from itertools import islice

def average(data) :
    
    result = 0
    count = 0
    for line in islice(data,1,None) :
        result += float(line[1])
        count += 1
    return float(result)/count
    
data1 = csv.reader(open('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population1b.csv'), 'excel')
data2 = csv.reader(open('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population2b.csv'), 'excel')
data3 = csv.reader(open('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population3b.csv'), 'excel')
data4 = csv.reader(open('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population4b.csv'), 'excel')
data5 = csv.reader(open('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population1p.csv'), 'excel')
data6 = csv.reader(open('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population2p.csv'), 'excel')
data7 = csv.reader(open('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population3p.csv'), 'excel')
data8 = csv.reader(open('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population4p.csv'), 'excel')




print average(data1)
print average(data2)
print average(data3)
print average(data4)
print average(data5)
print average(data6)
print average(data7)
print average(data8)

"""

def changetolist(data1):
    mylist = []
    for line in islice(data1, 1, None):
        mylist.append(float(line[1]))
    return mylist
a = changetolist(data1)
b = changetolist(data2)
c = changetolist(data3)
d = changetolist(data4)
e = changetolist(data5)
f = changetolist(data6)
g = changetolist(data7)
h = changetolist(data8)


res1 = stats.ttest_ind(a,b,equal_var = False)
res2 = stats.ttest_ind(c,d,equal_var = False)
res3 = stats.ttest_ind(e,f,equal_var = False)
res4 = stats.ttest_ind(g,h,equal_var = False)

print res1
print res2
print res3
print res4
"""
"""
if average(data1) < average(data2) :
    print True
else :
    print False
"""
    

    