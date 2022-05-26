
import numpy as np
import matplotlib.pyplot as plt
from math import *
from src.utils.operations import *

class EigenJacobi:
    def __init__(self, return_det):
        self.return_det = return_det
        self.feedback = "Sucesso"

    def eigenJacobiMethod(self, matrixA, limit=0.000001):
        if  isSymetric(matrixA) == False:
            self.feedback = "Autovalores por Jacobi é para matrizes simétricas apenas"
            raise ValueError("Autovalores por Jacobi é para matrizes simétricas apenas")

        A = matrixA
        shape = len(A) 
        X = np.identity(shape)
        greater, i, j = greaterValueOffDiagonal(A)
        while (greater > limit):
            P = pMatrixGen(A, i, j)
            A = P.T * A * P
            X = X * P
            greater, i, j = greaterValueOffDiagonal(A)
        det = self.get_det_if_needed(A)
        return A, X, det

    def get_det_if_needed(self, A):
        if(self.return_det == False):
            return None
        detA = 1
        for i in range(len(A)):
            detA = detA*A[i][i]

