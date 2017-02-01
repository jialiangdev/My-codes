# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 22:21:49 2016

@author: Jialiang Yu
"""

import pandas as pd
import pylab as pl
import numpy as np
from six import string_types
from sklearn.metrics import roc_curve, auc, f1_score
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
		return (x + np.random.normal(loc=0.0, scale=1e-4))
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


# read the data in

train_file = "Bank_Data_Train.csv"
#validation_file = "Bank_Data_Train.csv"
validation_file = "Kaggle_Public_Validation.csv"
train_size = 3482

data_train, target_train = data_processing(train_file)

data_train = data_train[0:train_size]
target_train = target_train[0:train_size]

data_validation, target_validation = data_processing(validation_file)

# replace categorical strings with 1-of-K coding and add a small amount of Gaussian noise so it follows Gaussian model assumption

data_train, data_validation = add_categorical(train=data_train,validation=data_validation,feature_str='FICO Range')

data_train, data_validation = add_categorical(train=data_train,validation=data_validation,feature_str='Loan Purpose')


#prepare plots
fig, ax = pl.subplots()


reg_type = "l2"
for sigma_sq in [1e-10, 100, 1e4]:
	# Describe classifier and regularization type
	logr = LogisticRegression(penalty=reg_type,C=1/sigma_sq,fit_intercept=True)
	# Train model
	logr.fit(X=data_train, y=target_train)
	# Predicted probabilities of label +1
	y_pred = logr.predict_proba(data_validation)[:,1]

	### ROC Curve ###
	# Find false and true positives of each target for various tresholds
	fpr, tpr, thresholds =roc_curve(target_validation, y_pred)
	# Area under the curve
	roc_auc = auc(fpr, tpr)
	print("New Regularization sigma_sq = %f" % sigma_sq)
	print("- Area under the ROC curve: %f" % roc_auc)
	# Get ROC values
	i = np.arange(len(tpr)) # index for df
	roc = pd.DataFrame({'fpr' : pd.Series(fpr, index=i),'tpr' : pd.Series(tpr, index = i), '1-fpr' : pd.Series(1-fpr, index = i), 'tf' : pd.Series(tpr - (1-fpr), index = i), 'thresholds' : pd.Series(thresholds, index = i)})
	roc.ix[(roc.tf-0).abs().argsort()[:1]]
	# Plot ROC values
	if reg_type == 'l2':
		reg_var = "\\sigma^2/\\sigma^2_w"
	else:
		reg_var = "\\lambda"
	pl.plot(roc.ix[:,1], roc.ix[:,4], label='Reg {reg_t},penalty ${reg_var} = {s}$'.format(reg_t=reg_type,reg_var=reg_var,s=sigma_sq))


pl.legend(loc='best')
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.title('Receiver operating characteristic')
#ax.set_xticklabels([])

pl.show()

