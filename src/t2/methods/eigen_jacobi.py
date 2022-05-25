
import numpy as np
import matplotlib.pyplot as plt
from math import *
from src.utils.operations import *

class EigenJacobi:
    def __init__(self):
        self.feedback = "Sucesso"

    def eigenJacobiMethod(self, matrixA, limit=0.000001):
        if  isSymetric(matrixA) == False:
            self.feedback = "Autovalores por Jacobi é para matrizes simétricas apenas"
            raise ValueError("Autovalores por Jacobi é para matrizes simétricas apenas")

        A = matrixA
        shape = np.shape(matrixA) 
        X = np.identity(shape)
        greater, i, j = greaterValueOffDiagonal(A)
        while (greater > limit):
            P = pMatrixGen(A, i, j)
            A = P.t * A * P
            X = X * P
            greater, i, j = greaterValueOffDiagonal(A)
        print(A, X)
        return A, X