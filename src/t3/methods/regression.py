from re import I
import numpy as np
import matplotlib.pyplot as plt
from math import *
from src.utils.operations import *

class Regression:
    def __init__(self, points):
        self.points = points
        self.feedback = "Sucesso"
        self.n = len(self.points)
        self.m = self.n -1
        self.x = [i[0] for i in self.points]
        self.y = [i[1] for i in self.points]

    def get_sum(self, arr):
        sum = 0
        for i in arr:
            sum += i
        return sum

    def get_squared_sum(self, arr):
        sum = 0
        for i in arr:
            sum += i*i
        return sum
    
    def get_multiplied_sum(self, arr1, arr2):
        sum = 0
        for i in arr1:
            sum += i*arr2[arr1.index(i)]
        return sum

    def linear_regression2(self, xp):
        p = []
        for i in self.x:
            p.append([1, i])

        P = np.matrix(p)
        A = np.dot(P.T, P)
        Y = np.array(self.y)
        C = np.dot(P.T, Y.T)
        Ai = np.linalg.inv(A)
        B = np.dot(Ai, C.T)
        a, b = B[1], B[0]
        plt.plot(self.x, self.y, 'ro')
        plt.xlabel('x')
        plt.ylabel('y')
        yp = a*xp + b
        plt.plot(xp, yp, 'bo')
        plt.show()
        return a*xp + b

    def linear_regression(self, xp):
        a11 = self.n
        a12 = self.get_sum(self.x)
        a21 = self.get_sum(self.x)
        a22 = self.get_squared_sum(self.x)

        c11 = self.get_sum(self.y)
        c21 = self.get_multiplied_sum(self.y, self.x)

        A = []
        A.append([a11, a12])
        A.append([a21, a22])

        C = []
        C.append(c11)
        C.append(c21)
        Ai = get_m2_inverse(A)
        if(Ai == 0):
            self.feedback = "Determinante de A = 0"
            raise ValueError("Determinante de A = 0")

        Ai = np.matrix(Ai)
        C = np.matrix(C)
        B = np.dot(Ai, C.T)

        a, b = B[1], B[0]
        plt.plot(self.x, self.y, 'ro')
        plt.xlabel('x')
        plt.ylabel('y')
        yp = a*xp + b
        plt.plot(xp, yp, 'bo')
        plt.show()
        return a*xp + b
