# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 09:48:28 2016

@author: Jialiang Yu
"""

import numpy as np

import csv

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, FastICA


M = 4
N = 3

#X = np.random.normal(size=[20,18])
#print X

A = [[2,0,1,3],[6,2,0,1],[0,1,4,6],[3,6,7,8]]
average = []
av = 0
for j in range(N):
    for i in range(M):
        av += A[i][j]
    result = float(av) / M
    average.append(result)
    av = 0
for j in range(N):
    for i in range(M):
        A[i][j] -= average[j]
U,s,V = np.linalg.svd(A,full_matrices=False) # SVD decomposition 
print U
print s
print V



"""
matrix = []
reader=csv.reader(open("E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW3\Q2.txt","rb"),delimiter=',')
data=list(reader)
for lst in data:
    mylist = []
    for i in range(len(lst)-1):
        mylist.append(int(lst[i]))
    matrix.append(mylist)

print matrix[681304]
#print np.matrix(matrix).shape

l = []
for i in range(681305):
    l.append(matrix[i][1])
rl = sorted(l)
print rl
"""




"""
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses

plt.scatter(x, y, s=area, c=colors, alpha=0.6)
plt.show()

"""

"""
rng = np.random.RandomState(42)
S = rng.standard_t(1.5, size=(20000, 2))
S[:, 0] *= 2.

# Mix data
A = np.array([[1, 1], [0, 2]])  # Mixing matrix

X = np.dot(S, A.T)  # Generate observations

pca = PCA()
S_pca_ = pca.fit(X).transform(X)

ica = FastICA(n_components = 5, algorithm='parallel', max_iter=100, tol=0.001)
S_ica_ = ica.fit(X).transform(X)  # Estimate the sources

S_ica_ /= S_ica_.std(axis=0)


###############################################################################
# Plot results

def plot_samples(S, axis_list=None):
    plt.scatter(S[:, 0], S[:, 1], s=2, marker='o', zorder=10,
                color='steelblue', alpha=0.5)
   
    plt.hlines(0, -5, 5)
    plt.vlines(0, -5, 5)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.xlabel('x')
    plt.ylabel('y')



axis_list = [pca.components_.T, ica.mixing_]
plt.subplot(2, 1, 1)
plot_samples(X / np.std(X), axis_list=axis_list)


plt.title('Observations')

plt.subplot(2, 1, 2)
plot_samples(S_ica_ / np.std(S_ica_))
plt.title('ICA recovered signals')

plt.subplots_adjust(0.09, 0.04, 0.94, 0.94, 0.26, 0.36)
plt.show()
"""









    




