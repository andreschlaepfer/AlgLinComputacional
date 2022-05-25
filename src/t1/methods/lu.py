import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import *
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot, linalg
from copy import deepcopy
from src.utils.operations import *

class LU:
    def decomposicao_LU(self, A, shouldReturnDet = True, return_det=False, show_warnings=True):
        L = np.eye(A)
        U = np.copy(A)  
        n = np.shape(U)[0] 
        j = 1
        for j in np.arange(n-1):
            for i in np.arange(j+1,n):  
                    L[i,j] = U[i,j]/U[j,j]  
                    for k in np.arange(j+1,n):  
                        U[i,k] = U[i,k] - L[i,j]*U[j,k]  
                    U[i,j] = 0
        det = self.get_determinant_if_needed(U, shouldReturnDet)
        return L, U, det

    def get_determinant_if_needed(self, U, shouldReturnDet):
        if(not shouldReturnDet):
            return "Não foi pedido que a determinante seja retornada"
        det = 1
        for i in range(U.shape[0]):
            for j in range(U.shape[1]):
                if (i == j):
                    det *= U[i][j]
        if (det == 0):
            print ("Matriz singular!")
        return det

    def solve(self, A, B):
        L, U, det = self.decomposicao_LU(A)  
        y = forward_substitution(L, B)    
        return back_substitution(U, y), det