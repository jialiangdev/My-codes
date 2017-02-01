# -*- coding: utf-8 -*-
"""
Created on Wed Mar 09 19:41:15 2016

@author: Jialiang Yu
"""
import xlwt
from tempfile import TemporaryFile
import csv
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from patsy import dmatrices
from sklearn.linear_model import LogisticRegression
from sklearn import naive_bayes
from sklearn import svm
from sklearn.cross_validation import cross_val_score
from scipy import stats
from pandas import ExcelWriter

data = pd.read_csv('E://Purdue Courses/Second semester/CS573 Data Mining/CS573 homework/Midterm/bank_data_new/input.csv',index_col=0)
test = pd.read_csv('E://Purdue Courses/Second semester/CS573 Data Mining/CS573 homework/Midterm/bank_data_new/test.csv',index_col=0)

"""
#linear regression

data.head()
print data.columns
print data.shape
print sm.show_versions()
print data.dtypes
lm = smf.ols(formula='Status ~  Amount_Requested + Interest_Rate_Percentage + Loan_Length_in_Months + Loan_Purpose + Monthly_PAYMENT + Total_Amount_Funded + Debt_To_Income_Ratio_Percentage', data=data).fit()
print lm.params
print lm.summary()

log = smf.logit(formula='Status ~  Amount_Requested + Interest_Rate_Percentage + Loan_Length_in_Months + Loan_Purpose + Monthly_PAYMENT + Total_Amount_Funded + Debt_To_Income_Ratio_Percentage', data=data).fit()
print log.params
print log.summary()
"""
"""
#1 of K encoding

train = pd.read_csv('E://Purdue Courses/Second semester/CS573 Data Mining/CS573 homework/Midterm/bank_data_new/Bank_Data_Train.csv',index_col=0)
test =  pd.read_csv('E://Purdue Courses/Second semester/CS573 Data Mining/CS573 homework/Midterm/bank_data_new/Bank_Data_Test.csv',index_col=0)

encoded = pd.get_dummies(pd.concat([train['FICO Range'],test['FICO Range']], axis=0), \
                            prefix = 'FICO Range', dummy_na=True)
train_rows = train.shape[0]
train_encoded = encoded.iloc[:train_rows, :]
test_encoded = encoded.iloc[train_rows:, :]

encoded2 = pd.get_dummies(pd.concat([train['Loan Purpose'], test['Loan Purpose']], axis=0), \
                            prefix = 'Loan Purpose', dummy_na = True)
train_rows = train.shape[0]
train_encoded2 = encoded2.iloc[:train_rows, :]
test_encoded2 = encoded2.iloc[train_rows:, :]

writer = ExcelWriter('E://Purdue Courses/Second semester/CS573 Data Mining/CS573 homework/Midterm/bank_data_new/training_data.xlsx')
train_encoded.to_excel(writer,'Sheet1')
train_encoded2.to_excel(writer,'Sheet2')
test_encoded.to_excel(writer,'Sheet3')
test_encoded2.to_excel(writer,'Sheet4')

writer.save()


"""



# data input, split training set and result
target,train_set = dmatrices('Status ~  Amount_Requested + Interest_Rate_Percentage + \
              Loan_Length_in_Months + Loan_Purpose + Monthly_PAYMENT + \
              Total_Amount_Funded + Debt_To_Income_Ratio_Percentage + FICO', data, return_type='dataframe')
target = np.ravel(target)  
"""
model = LogisticRegression()
model = model.fit(train_set,target)
print model.score(train_set,target)
print pd.DataFrame(zip(train_set.columns, np.transpose(model.coef_)))
predict_value = model.predict(test)
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')

for i,e in enumerate(predict_value):
    sheet1.write(i,1,e)

name = "E://Purdue Courses/Second semester/CS573 Data Mining/CS573 homework/Midterm/bank_data_new/random.xls"
book.save(name)
book.save(TemporaryFile())
"""

#evaluate the model using 10-fold cross-validation
#logistic
print "Logistic"
Logistic_scores = cross_val_score(LogisticRegression(), train_set, target, scoring='f1', cv=50)
print Logistic_scores
print Logistic_scores.mean()


#svm-linear
print "svm"
svm_scores = cross_val_score(svm.LinearSVC(),train_set, target, scoring='f1', cv = 50)
print svm_scores
print svm_scores.mean()

#svm-gaussian
print "svm"
svm_scores2 = cross_val_score(svm.NuSVC(),train_set, target, scoring='f1', cv = 50)
print svm_scores2
print svm_scores2.mean()


#NBC
print "NBC"
#My NBC
nbc_scores = cross_val_score(naive_bayes.MultinomialNB(alpha = 2), train_set, target, scoring = 'f1', cv = 50)
print nbc_scores
print nbc_scores.mean()

#t-test
t,prob = stats.ttest_ind(Logistic_scores, svm_scores)
print "Logistic and svm_linear is: %s" % t,prob

t2,prob2 = stats.ttest_ind(Logistic_scores, svm_scores2)
print "Logistic and svm_gaussian is: %s" % t2,prob2

t3,prob3 = stats.ttest_ind(Logistic_scores, nbc_scores)
print "Logistic and nbc is: %s" % t3,prob3

t4,prob4 = stats.ttest_ind(nbc_scores, svm_scores)
print "nbc and svm_linear is: %s" % t4,prob4

t5,prob5 = stats.ttest_ind(nbc_scores, svm_scores2)
print "nbc and svm_gaussian is: %s" % t5,prob5

t6,prob6 = stats.ttest_ind(svm_scores, svm_scores2)
print "svm_linear and svm_gaussian is: %s" % t6,prob6











