import operator
import numpy as np
from functools import reduce
import matplotlib.pyplot as pl


# PARAFAC decomposition from http://stackoverflow.com/questions/36541154/how-to-use-scikit-tensor-in-python
def ribs(loadings):
  '''
  Convert a list of n loading matrices [A_{fi}, B_{fj}, C_{fk}, ...] into ribs
  [A_{fi11...}, B_{f1j1...}, C_{f11k...}, ...]. These ribs can be multiplied
  with numpy broadcasting to fill a tensor with data.
  '''
  loadings = [np.atleast_2d(l) for l in loadings]
  nfactors = loadings[0].shape[0]
  assert np.alltrue([l.ndim == 2 and l.shape[0] == nfactors for l in loadings])
  ribs = []
  for mi in range(len(loadings)):
    shape = [nfactors] + [-1 if fi == mi else 1 for fi in range(len(loadings))]
    ribs.append(loadings[mi].reshape(shape))
  return ribs

def para_compose(ribs):
  return np.sum(reduce(operator.mul, ribs), axis=0)

def parafac_base(x, nfactors, max_iter=100):
  '''
  PARAFAC is a multi-way tensor decomposition method. Given a tensor X, and a
  number of factors nfactors, PARAFAC decomposes the X in n factors for each
  dimension in X using alternating least squares:

  X_{ijk} = \sum_{f} a_{fi} b_{fj} c_{fk} + e_{ijk}

  PARAFAC can be seen as a generalization of PCA to higher order arrays [1].
  Return a ([a, b, c, ...], mse)

  [1] Rasmus Bro. PARAFAC. Tutorial and applications. Chemometrics and
  Intelligent Laboratory Systems, 38(2):149-171, 1997.
  '''
  loadings = [np.random.rand(nfactors, n) for n in x.shape]

  last_mse = np.inf
  for i in range(max_iter):
    # 1) forward (predict x)
    xhat = para_compose(ribs(loadings))

    # 2) stopping?
    mse = np.mean((xhat - x) ** 2)
    if last_mse - mse < 1e-10 or mse < 1e-20:
      break
    last_mse = mse

    for mode in range(len(loadings)):
      print('iter: %d, dir: %d' % (i, mode))
      # a) Re-compose using other factors
      Z = ribs([l for li, l in enumerate(loadings) if li != mode])
      Z = reduce(operator.mul, Z)

      # b) Isolate mode
      Z = Z.reshape(nfactors, -1).T # Z = [long x fact]
      Y = np.rollaxis(x, mode)
      Y = Y.reshape(Y.shape[0], -1).T # Y = [mode x long]

      # c) least squares estimation: x = np.lstsq(Z, Y) -> Z x = Y
      new_fact, _, _, _ = np.linalg.lstsq(Z, Y)
      loadings[mode] = new_fact
  if not i < max_iter - 1:
    print('parafac did not converge in %d iterations (mse=%.2g)' %
      (max_iter, mse))
  return loadings, mse

Xlist = []

maxi = 0
maxj = 0
maxk = 0
with open("traffic.dat") as f:
  for line in f.readlines():
    i,j,k,Xijk = list(map(int, line.split("\t")))
    maxi = max(i,maxi)
    maxj = max(j,maxj)
    maxk = max(k,maxk)
    Xlist.append((i,j,k,Xijk))

X = np.zeros((maxi+1, maxj+1, maxk+1))

for i,j,k,Xijk in Xlist:
  X[i,j,k] = Xijk

loadings,mse = parafac_base(x=X,nfactors=2)

A=loadings[0]
B=loadings[1]
C=loadings[2]
print A[0].shape
print B[0].shape
print C[0].shape

pl.legend(loc='best')
pl.xlabel('Train Samples')
pl.ylabel('F1 Score')
pl.ylim([0, 1])
pl.title('score of a,b,c')

x_i = []
y_i = []
z_i = []

for i in range(len(A[0])):
    x_i.append(i)
for j in range(len(B[0])):
    y_i.append(j)
for r in range(len(C[0])):
    z_i.append(r)
    
pl.plot(x_i, A[0])
pl.plot(x_i, A[1])



#ax.set_xticklabels([])
pl.savefig('E:\\Purdue Courses\\Second semester\\CS573 Data Mining\\CS573 homework\\HW5\\2.png', dpi = 1000)
pl.show()
















