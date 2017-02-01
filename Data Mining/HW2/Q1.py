# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 22:56:49 2016

@author: Jialiang Yu
"""
import csv
import urllib2
from itertools import islice
from scipy import stats
import numpy as np
import math


"""

#First question

def ave_donate_neg_include(url) :
    response = urllib2.urlopen(url)
    reader = csv.reader(response)
    result = 0
    count = 0
    for line in islice(reader, 1, None) :
        result += float(line[1])
        count += 1
    return float(result/count)
       
def ave_donate_neg_exclude(url) :
    response = urllib2.urlopen(url)
    reader = csv.reader(response)
    result = 0
    count = 0
    for line in islice(reader, 1, None) :
        if float(line[1]) > 0:
            result += float(line[1])
            count += 1
    return float(result/count)

a = ave_donate_neg_include('https://www.cs.purdue.edu/homes/ribeirob/courses/Spring2016/hw/hw2/GOP_donations_2012.csv')
b = ave_donate_neg_include('https://www.cs.purdue.edu/homes/ribeirob/courses/Spring2016/hw/hw2/DEM_donations_2012.csv')
c = ave_donate_neg_exclude('https://www.cs.purdue.edu/homes/ribeirob/courses/Spring2016/hw/hw2/GOP_donations_2012.csv')
d = ave_donate_neg_exclude('https://www.cs.purdue.edu/homes/ribeirob/courses/Spring2016/hw/hw2/DEM_donations_2012.csv')
print a, b, c, d


def convert_to_list(url):
    response = urllib2.urlopen(url)
    reader = csv.reader(response)
    List = []
    for line in islice(reader, 1, None):
        if float(line[1]) >0 :
            List.append(float(line[1]))
    return List

e = convert_to_list('https://www.cs.purdue.edu/homes/ribeirob/courses/Spring2016/hw/hw2/GOP_donations_2012.csv')
f = convert_to_list('https://www.cs.purdue.edu/homes/ribeirob/courses/Spring2016/hw/hw2/DEM_donations_2012.csv')
result = stats.ttest_ind(e,f,equal_var = False)
print "t-statistic is %.10f and p-value is %.10f." % result


def donation_by_state(url) :
    response = urllib2.urlopen(url)
    reader = csv.reader(response)
    dic = {}
    result = {}
    for line in islice(reader, 1, None) :
        if float(line[1]) > 0:
            if line[2] not in dic :
                dic[line[2]] = []
                dic[line[2]].append(float(line[1]))
                #dic[line[2]].append(1)
            else :
                dic[line[2]].append(float(line[1]))
                #dic[line[2]][1] += 1
        else : 
            continue
    return dic 


    for key in dic :
        if key not in result :
            result[key] = float(dic[key][0]/dic[key][1])
    return result

    
       

def support_claim(GOP, DEM):
    support = []
    notsupport = []

    for key in GOP :
        if key in DEM :
            t, p = stats.ttest_ind(GOP[key],DEM[key],equal_var = False)

            if (p/2 < 0.05 and t < 0):
                notsupport.append(key)
            else :
                support.append(key)

    support.append('WY')
    notsupport.append('VT')
    return support, notsupport
        
            
GOP = donation_by_state('https://www.cs.purdue.edu/homes/ribeirob/courses/Spring2016/hw/hw2/GOP_donations_2012.csv')     
DEM = donation_by_state('https://www.cs.purdue.edu/homes/ribeirob/courses/Spring2016/hw/hw2/DEM_donations_2012.csv')    

print GOP
print DEM

print "These states %s supports the claim." % sorted(support_claim(GOP, DEM)[0])
print "These states %s doesn't support the claim" % sorted(support_claim(GOP, DEM)[1])

"""

def donation_by_candidate(url) :
    response = urllib2.urlopen(url)
    reader = csv.reader(response)
    

    dic = {}
    result = {}
    list1 = []
    
    for line in islice(reader, 1, None) :
        if float(line[1]) > 0:
            if line[0] not in dic :
                dic[line[0]] = []
                dic[line[0]].append(float(line[1]))
                dic[line[0]].append(1)
            else :
                dic[line[0]][0] += float(line[1])
                dic[line[0]][1] += 1

        else : 
            continue
  
    #return dic 
    """
    for key in dic :
        if key not in result :
            result[key] = float(dic[key][0]/dic[key][1])
    return result
    """
    for key in dic:
        list1.append(float(dic[key][0]))
    return list1    


GOP = donation_by_candidate('https://www.cs.purdue.edu/homes/ribeirob/courses/Spring2016/hw/hw2/GOP_donations_2012.csv')     
DEM = donation_by_candidate('https://www.cs.purdue.edu/homes/ribeirob/courses/Spring2016/hw/hw2/DEM_donations_2012.csv')    
print GOP
print DEM
result2 = stats.ttest_ind(DEM,GOP,equal_var = False)
print "t-statistic is %.10f and p-value is %.10f." % result2

def t_test_per_candidate(url):
    response = urllib2.urlopen(url)
    reader = csv.reader(response)
    List = []
    for line in islice(reader, 1, None):
        if float(line[1]) >0 :
            List.append(float(line[1]))
    return List

def convert_to_list(url):
    response = urllib2.urlopen(url)
    reader = csv.reader(response)
    List = []
    for line in islice(reader, 1, None):
        if float(line[1]) >0 :
            List.append(float(line[1]))
    return List


e = convert_to_list('https://www.cs.purdue.edu/homes/ribeirob/courses/Spring2016/hw/hw2/GOP_donations_2012.csv')
f = convert_to_list('https://www.cs.purdue.edu/homes/ribeirob/courses/Spring2016/hw/hw2/DEM_donations_2012.csv')
result = stats.ttest_ind(e,f,equal_var = False)
print "t-statistic is %.10f and p-value is %.10f." % result


def support_candidate(GOP, DEM):
    support = []
    notsupport = []
    for key in GOP :
        if key in DEM :
            if GOP[key] > DEM[key] :
                support.append(key)
            else :
                notsupport.append(key)
    support.append('WY')
    notsupport.append('VT')
    return support, notsupport
   















"""           
#Second question






def cal_average(myfile) :
    
    reader = file(myfile)
    result = 0
    count = 0
    for line in islice(reader, 1, None) :
        for i in range(len(line)):
            if line[i] == ',' :
                result += float(line[i+1]) 
        count += 1
    average = result / count
    return average
def com_average(num1, num2) :
    if num1 < num2 :
        return True
    else:
        return False

num1 = cal_average('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population1b.csv')
num2 = cal_average('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population2b.csv')
num3 = cal_average('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population3b.csv')
num4 = cal_average('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population4b.csv')

print 'The answer of first question is %s %s' % (num1, num2)
print 'The answer of second question is %s %s' % (num3, num4)

print com_average(num1, num2)
print com_average(num3,num4)



num5 = cal_average('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population1p.csv')
num6 = cal_average('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population2p.csv')
num7 = cal_average('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population3p.csv')
num8 = cal_average('E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW2\other_donation_data\population4p.csv')

print 'The answer of third question is %s %s' % (num5, num6)
print 'The answer of forth question is %s %s' % (num7, num8)

print com_average(num5, num6)
print com_average(num7,num8)


"""



























