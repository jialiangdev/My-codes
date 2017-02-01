# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 20:37:36 2016

@author: Jialiang Yu
"""


import csv
import numpy as np
import pandas as pd
from pandas import ExcelWriter
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from patsy import dmatrices
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score


train = pd.read_csv('E://Purdue Courses/Second semester/CS573 Data Mining/CS573 homework/Midterm/bank_data_new/Bank_Data_Train.csv',index_col=0)
test =  pd.read_csv('E://Purdue Courses/Second semester/CS573 Data Mining/CS573 homework/Midterm/bank_data_new/Bank_Data_Test.csv',index_col=0)

encoded = pd.get_dummies(pd.concat([train['FICO Range'],test['FICO Range']], axis=0), \
                            prefix = 'FICO Range', dummy_na=True)
train_rows = train.shape[0]
train_encoded = encoded.iloc[:train_rows, :]
test_encoded = encoded.iloc[train_rows:, :]

#print train_encoded
#print test_encoded

encoded2 = pd.get_dummies(pd.concat([train['Loan Purpose'], test['Loan Purpose']], axis=0), \
                            prefix = 'Loan Purpose', dummy_na = True)
train_rows = train.shape[0]
train_encoded2 = encoded2.iloc[:train_rows, :]
test_encoded2 = encoded2.iloc[train_rows:, :]

#print train_encoded2
#print test_encoded2


writer = ExcelWriter('E://Purdue Courses/Second semester/CS573 Data Mining/CS573 homework/Midterm/bank_data_new/training_data.xlsx')
train_encoded.to_excel(writer,'Sheet1')
train_encoded2.to_excel(writer,'Sheet2')
test_encoded.to_excel(writer,'Sheet3')
test_encoded2.to_excel(writer,'Sheet4')



writer.save()





















