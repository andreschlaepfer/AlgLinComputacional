from asyncio.windows_events import NULL
import math
import numpy as np
from src.utils.operations import *
class Cholesky:
    def __init__(self, return_det):
        self.return_det = return_det
        self.feedback = "Sucesso"

    def decomposicao_Cholesky(self, A):
        n = len(A)
        Lo = [[0.0] * n for i in range(n)]
        for i in range(n):
            for k in range(i+1):
                tmp_sum = sum(Lo[i][j] * Lo[k][j] for j in range(k))
                if (i == k): 
                    Lo[i][k] = math.sqrt(A[i][i] - tmp_sum)
                else:
                    Lo[i][k] = (1.0 / Lo[k][k] * (A[i][k] - tmp_sum))
        det = self.determinant(Lo)
        return Lo, det

    def determinant(self, L):
        if (self.return_det == False):
            return NULL
        det = 1
        for i in range(len(L)):
            det = det*L[i][i]
        return det*det
    
    def solve(self, A, B):
        Lo, det = self.decomposicao_Cholesky(A) 
        Lo = np.matrix(Lo)
        Lot = Lo.T 
        y = forward_substitution(Lo, B)    
        return back_substitution(Lot, y), det

