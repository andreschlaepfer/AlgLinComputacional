import math
import numpy as np
class Cholesky:
    def decomposicao_Cholesky(self, A):
        n = np.shape(A)[0]
        if n != np.shape(A)[1]:
            return "Matriz A não é quadrada!"

        L = [[0 for x in range(n + 1)]
                        for y in range(n + 1)];

        for i in range(n):
            for j in range(i + 1):
                sum1 = 0;
                if (j == i):
                    for k in range(j):
                        sum1 += pow(L[j][k], 2);
                    L[j][j] = int(math.sqrt(A[j][j] - sum1));
                else:
                    for k in range(j):
                        sum1 += (L[i][k] *L[j][k]);
                    if(L[j][j] > 0):
                        L[i][j] = int((A[i][j] - sum1) /
                                                L[j][j]);
        return L

    def determinant(self, L):
        det = 1
        for i in range(L.shape[0]):
            det = det*L[i][i]
        return det*det

