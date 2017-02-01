# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 21:47:19 2016

@author: Jialiang Yu
"""

import csv
import numpy as np
from scipy import sparse
from scipy import sparse as ssp
import matplotlib.pyplot as plt
from scipy.sparse import linalg
from sklearn.decomposition import PCA, FastICA
from sklearn.preprocessing import StandardScaler

matrix = []
M = 5488
N = 9543
A = [[0 for i in range(N)] for j in range(M)]


reader=csv.reader(open("E:\Purdue Courses\Second semester\CS573 Data Mining\CS573 homework\HW3\Q2.txt","rb"),delimiter=',')
data=list(reader)
for lst in data:
    mylist = []
    for i in range(len(lst)-1):
        mylist.append(int(lst[i]))
    matrix.append(mylist)

for i in range(681305):
        A[matrix[i][0]][matrix[i][1]] = float(matrix[i][2])

U, s, V = linalg.svds(A, k = 10) #performs a sparse matrix SVD using k_latent latent factors.
print np.shape(A)
print np.shape(U)
print np.shape(s)
print np.shape(V)
#pca = PCA()


average = []
av = 0
for j in range(9543):
    for i in range(5488):
        av += A[i][j]
    result = float(av) / 5488
    average.append(result)
    av = 0
for j in range(9543):
    for i in range(5488):
        A[i][j] -= average[j]



sc = StandardScaler()
A_T_std = sc.fit_transform(np.transpose(A))
#S_pca_ = pca.fit(A).transform(A)  # apply the dimensionility reduction on X
ica = FastICA(n_components=2, algorithm='parallel', whiten=True,  fun='logcosh', fun_args=None, max_iter=100, tol=0.01, w_init=None, random_state=None)
S_ica_ = ica.fit(A_T_std).transform(A_T_std)  #estimate the sources
#S_ica_ /= S_ica_.std(axis=0)
#print S_pca_
#print np.shape(S_ica_)





###############################################################################
# Plot results

def plot_samples(S, axis_list=None):
    plt.scatter(S[:, 0], S[:, 1], s=2, marker='.', zorder=5,
                color='steelblue', alpha=0.5)
   
    plt.hlines(0, -3, 3)
    plt.vlines(0, -3, 3)
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.xlabel('x')
    plt.ylabel('y')



#axis_list = [pca.components_.T, ica.mixing_]
#plt.subplot(2, 1, 1)
#plot_samples(A / np.std(A))
#plt.title('Observations')

plt.subplot(1, 1, 1)
plot_samples(S_ica_ / np.std(S_ica_))
plt.title('ICA recovered signals')
highlightpoint = [111,288,102,291]
for point in highlightpoint:
    plt.plot(S_ica_[point][0], S_ica_[point][1], marker = 'o', markerfacecolor = 'red', markersize = 2)
    plt.annotate(point, (S_ica_[point][0], S_ica_[point][1]))
plt.savefig('E:\\Purdue Courses\Second semester\\CS573 Data Mining\\CS573 homework\\HW3\\program\\testplot2.png', dpi = 3000)










