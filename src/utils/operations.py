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
    raise ValueError("Erro em gerray array aleatorio. Tamanho passado deve ter 2 valores")
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
    for i in range(len(A)):
        l_sum = 0
        col_sum = 0
        for j in range(len(A)):
            if (i != j):
                l_sum += math.fabs(A[i][j])
                col_sum += math.fabs(A[j][i])

        if(A[i][i] < l_sum or A[i][i] < col_sum):
            return False

    return True

def get_residue(prevX, currX):
  numerador = linalg.norm(currX - prevX)
  denominador = linalg.norm(currX)
  return numerador/denominador

def greaterValueOffDiagonal(matrixA):
  shapeA = len(matrixA)
  greaterValue = 0
  greaterValue_i = 0
  greaterValue_j = 0

  for i in range(shapeA):
    for j in range(shapeA):
      if (i != j):
        value = abs(matrixA[i][j])
        if value > greaterValue:
          greaterValue = value
          greaterValue_i = i
          greaterValue_j = j
  return greaterValue, greaterValue_i, greaterValue_j

def pMatrixGen(A, i, j):
  if (A[i][i] != A[j][j]):
    phi = 1. / 2. * math.atan((2 * A[i][j]) / (A[i][i] - A[j][j])) 
  else:
    phi = math.pi / 4
  shape = len(A) 
  p = np.identity(shape)
  p[i][i] = math.cos(phi)
  p[i][j] = -math.sin(phi)
  p[j][i] = math.sin(phi)
  p[j][j] = math.cos(phi)
  return p


def isSymetric(A):
    A = np.matrix(A)
    matrixB = A.transpose()

    if A.shape == matrixB.shape:
        if (A == matrixB).all():
            return True
        else:
            return False    
    else:
        return False