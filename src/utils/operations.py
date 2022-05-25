import math
import copy
from re import M
import numpy as np
from numpy import array, zeros, diag, diagflat, dot, linalg

def det(A):
    n = len(A)
    AM = copy.deepcopy(A)
    for fd in range(n): 
        for i in range(fd+1,n): 
            if AM[fd][fd] == 0: 
                AM[fd][fd] == 1.0e-18 
            crScaler = AM[i][fd] / AM[fd][fd] 

            for j in range(n): 
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
     
    product = 1.0
    for i in range(n):
        product *= AM[i][i]  
    return product

def get_m2_inverse(A):
    detA = (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
    if(detA == 0):
        return 0
    m = 1/detA
    a00 = A[1][1]*m
    a01 = A[0][1]*m
    a10 = A[1][0]*m
    a11 = A[1][1]*m
    Ai = []
    Ai.append([a00, a01])
    Ai.append([a10, a11])
    return Ai


def forward_substitution(L, b):
    n = L.shape[0]
    y = np.zeros_like(b, dtype=np.double); 
    y[0] = b[0] / L[0, 0]   
    for i in range(1, n):
        y[i] = (b[i] - np.dot(L[i,:i], y[:i])) / L[i,i]        
    return y

def back_substitution(U, y):   
    n = U.shape[0]
    x = np.zeros_like(y, dtype=np.double);
    x[-1] = y[-1] / U[-1, -1]
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - np.dot(U[i,i:], x[i:])) / U[i,i]      
    return x

def random_array(shape):
  import random
  random.seed()
  if len(shape) != 2:
    raise ValueError("Shape must have two values!")
  res = []
  for i in range(shape[0]):
    res.append([])
    for j in range(shape[1]):
      res[i].append(random.random())
  return np.array(res)

def is_definite_positive (A):
  if A.shape[0] != A.shape[1]:
    return False
  for k in range(1, A.shape[0] + 1):
    determinant = det(A.submatrix((k,k)))
    if (determinant < 0):
      return False
  return True

def is_diag_dominant(A):
  dom = zeros((A.shape[0], 1))
  for i in range(A.shape[0]):
    for j in range(A.shape[1]):
      if (i != j):
        dom[i][0] += abs(A[i][j])
  for i in range(A.shape[0]):
    for j in range(A.shape[1]):
      if (i == j):
        if (abs(A[i][j]) < dom[i][0]):
          return False
  return True

def get_residue(prevX, currX):
  numerador = linalg.norm(currX - prevX)
  denominador = linalg.norm(currX)
  return numerador/denominador