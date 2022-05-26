import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import *
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot, linalg
from copy import deepcopy
from src.utils.operations import *

class GaussSeidel:
    def __init__(self):
        self.feedback = "Sucesso"

    def procedimento_iterativo_GaussSeidel(self, A, B, tol, limit = 500):
        counter = 0
        r_logs = []
        if (not is_diag_dominant(A)):
            if (not is_definite_positive(A)):
                self.feedback = "O método de Gauss-Seidel não irá convergir!"
                return None, 0, r_logs
        prevX = random_array(B.shape)
        r = 1000
        n = B.shape[0]
        while (counter <= limit):
            X = zeros(B.shape)
            for i in range(X.shape[0]):
                X[i][0] = B[i][0]
            for j in range(0, i):
                X[i][0] -= A[i][j]*X[j][0]
            for j in range(i+1, n):
                X[i][0] -= A[i][j]*prevX[j][0]
            X[i][0] /= A[i][i]
            r = get_residue(prevX, X)
            r_logs += [r]
            if(get_residue(prevX, X) <= tol):
                return X, counter, r_logs
            prevX = deepcopy(X)
        return X, counter, r_logs