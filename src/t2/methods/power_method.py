import numpy as np
import matplotlib.pyplot as plt
from math import *
from src.utils.operations import *

class PowerMethod:
    def __init__(self):
        self.feedback = "Sucesso"
    
    def eigenPowerMethod(matrixA, limit=0.0000001):
        x = np.random.rand((len(matrixA), 1))
        x[0][0] = 1
        r = 1000
        lambda_i = limit
        while (r > limit):
            y = np.dot(matrixA, x)
            new_lambda_i = y[0][0]
            x = y / new_lambda_i
            r = abs(new_lambda_i - lambda_i) / abs(new_lambda_i)
            lambda_i = new_lambda_i
        return lambda_i, x