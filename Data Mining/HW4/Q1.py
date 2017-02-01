# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import pylab as pl
import numpy as np
from six import string_types
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def float_or_str(x):
	if isfloat(x):
		return (x)
	else:
		return (-1)


def percent_to_float(x):
	if isfloat(x):
		return (x/100)
	else:
		return float(x.strip('%'))/100

def add_noise(x):
	if not isinstance(x, string_types):
		return (x + np.random.normal(loc=0.0, scale=1e-3))
	else:
		return (x)


def data_processing(filename):
	# Read file (must be in UFT-8 if using python version >= 3)
	df = pd.read_csv(filename)

	# print (df.head()) # check feature ids

	df['Interest Rate Percentage'] = [percent_to_float(i) for i in df['Interest Rate Percentage']]

	df['Debt-To-Income Ratio'] = [percent_to_float(i) for i in df['Debt-To-Income Ratio Percentage']]

	features_to_keep = ['Amount Requested','Interest Rate Percentage','Loan Purpose','Loan Length in Months',
	                    'Monthly PAYMENT','Total Amount Funded','FICO Range','Debt-To-Income Ratio Percentage']

    # convert interger values to float (helps avoiding optimization implementation issues)
	for feature in features_to_keep:
		if feature not in ['FICO Range','Loan Purpose']:
			df[feature] = [float(i) for i in df[feature]]

	# Scale values
	df['Total Amount Funded'] /= max(df['Total Amount Funded'])
	df['Amount Requested'] /= max(df['Amount Requested'])
	df['Loan Length in Months'] /= max(df['Loan Length in Months'])
	df['Monthly PAYMENT'] /= max(df['Monthly PAYMENT'])

    # Interaction terms
	df['Total Amount Funded * Requested'] = df['Total Amount Funded']*df['Total Amount Funded']
	df['Total Amount Funded * Requested'] /= max(df['Total Amount Funded'])

	df['Interest Rate Percentage * Monthly PAYMENT'] = df['Interest Rate Percentage']*df['Monthly PAYMENT']
	df['Interest Rate Percentage * Monthly PAYMENT'] /= max(df['Interest Rate Percentage * Monthly PAYMENT'])


	target_var = [float_or_str(i) for i in df['Status']]

	# create a clean data frame for the regression
	data = df[features_to_keep].copy()
	
	data['intercept'] = 1.0

	return (data,target_var)

def add_categorical(train, validation, feature_str):
	# encode categorical features
	encoded = pd.get_dummies(pd.concat([train[feature_str],validation[feature_str]], axis=0))#, dummy_na=True)
	train_rows = train.shape[0]
	train_encoded = encoded.iloc[:train_rows, :]
	validation_encoded = encoded.iloc[train_rows:, :] 

	train_encoded_wnoise = train_encoded.applymap(add_noise)
	validation_encoded_wnoise = validation_encoded.applymap(add_noise)

	train.drop(feature_str,axis=1, inplace=True)
	validation.drop(feature_str,axis=1, inplace=True)

	train = train.join(train_encoded_wnoise.ix[:, :])
	validation = validation.join(validation_encoded_wnoise.ix[:, :])

	return (train,validation)


train_file = "Bank_Data_Train.csv"
validation_file = "Kaggle_Public_Validation.csv"

train_sizes = [50, 100,300,600,1000,1500,2000, 2500, 3000]
F1_scores_validation = []
F1_scores_train = []

# L2 Regularization penalty \\sigma^2/\\sigma^2_\\beta = sigma_sq
#sigma_sq = 10.0#1e+3
#sigma_sq = 1
reg_type = "l2"
reg_var = "\\sigma^2/\\sigma^2_w"


#for train_size in train_sizes:

# read the data in
train_size = 3000

rr = [10 ** i for i in range(-10,10)]

for sigma_sq in rr:
    
    data_train, target_train = data_processing(train_file)
    data_validation, target_validation = data_processing(validation_file)
    data_train = data_train[0:train_size]
    target_train = target_train[0:train_size]
    # replace categorical strings with 1-of-K coding and add a small amount of Gaussian noise so it follows Gaussian model assumption
    data_train, data_validation = add_categorical(train=data_train,validation=data_validation,feature_str='FICO Range')
    data_train, data_validation = add_categorical(train=data_train,validation=data_validation,feature_str='Loan Purpose')
    # Describe classifier and regularization type
    logr = LogisticRegression(penalty=reg_type,C=1/sigma_sq,fit_intercept=True)
    # Train model
    logr.fit(X=data_train, y=target_train)
    # Predicted probabilities of label +1
    #     0.35 is an arbitrary number
    y_pred_validation = (logr.predict_proba(data_validation)[:,1] > 0.35) + 0
    y_pred_train = (logr.predict_proba(data_train)[:,1] > 0.35) + 0
    f1score_validation = f1_score(target_validation, y_pred_validation)
    F1_scores_validation.append(f1score_validation)
    f1score_train = f1_score(target_train, y_pred_train)
    F1_scores_train.append(f1score_train)

    #prepare plots
fig, ax = pl.subplots()
    
#pl.plot(train_sizes, F1_scores_train, label='F1 over {type_val}, {type_pen} penalty ${reg_var} = {s}$'.format(type_val="training",type_pen=reg_type.upper(),reg_var=reg_var,s=sigma_sq),color="blue")
#pl.plot(train_sizes, F1_scores_validation, label='F1 over {type_val}, {type_pen} penalty ${reg_var} = {s}$'.format(type_val="validation",type_pen=reg_type.upper(),reg_var=reg_var,s=sigma_sq),color="red")
pl.semilogx(rr, F1_scores_train, label='F1 score train',color="blue")
pl.semilogx(rr, F1_scores_validation, label='F1 score validation',color="red")

def find_second(F1_scores_validation):
    mylist = []
    for num in F1_scores_validation:
        if num < 0.675:
            mylist.append(num)
        aa = sorted(mylist, reverse = True)
    return aa[0]
    
pl.semilogx(rr[F1_scores_validation.index(find_second(F1_scores_validation))],find_second(F1_scores_validation), color = "green", marker = 'o')
print (rr[F1_scores_validation.index(find_second(F1_scores_validation))],find_second(F1_scores_validation))
pl.legend(loc='best')
#pl.xlabel('Training Data Size')
#pl.xlabel(sigma_sq)
pl.ylabel('F1 Score')
pl.title('F1 Score x Training Data Size')

pl.show()
