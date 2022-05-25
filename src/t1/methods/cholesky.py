from asyncio.windows_events import NULL
import math
import numpy as np
from src.utils.operations import *
class Cholesky:
    def __init__(self, return_det):
        self.return_det = return_det
        self.feedback = "Sucesso"

    def decomposicao_Cholesky(self, A):
        n = np.shape(A)[0]
        if n != np.shape(A)[1]:
            self.feedback  = "Matriz A não é quadrada!"
            return

        Lo = [[0 for x in range(n + 1)]
                        for y in range(n + 1)]

        for i in range(n):
            for j in range(i + 1):
                sum1 = 0
                if (j == i):
                    for k in range(j):
                        sum1 += pow(Lo[j][k], 2)
                    Lo[j][j] = int(math.sqrt(A[j][j] - sum1))
                else:
                    for k in range(j):
                        sum1 += (Lo[i][k] *Lo[j][k])
                    if(Lo[j][j] > 0):
                        Lo[i][j] = int((A[i][j] - sum1) /
                                                Lo[j][j])
        


        det = self.determinant(Lo)
        return Lo, det

    def determinant(self, L):
        if (self.return_det == False):
            return NULL
        det = 1
        for i in range(L.shape[0]):
            det = det*L[i][i]
        return det*det
    
    def solve(self, A, B):
        Lo, det = self.decomposicao_Cholesky(A) 
        Lot = Lo.T 
        y = forward_substitution(Lo, Lot)    
        return back_substitution(Lot, y), det

