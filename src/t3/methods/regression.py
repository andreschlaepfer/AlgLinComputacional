from tkinter import N
import numpy as np
import matplotlib.pyplot as plt
from math import *
from src.utils.operations import *

class Regression:
    def __init__(self, points):
        self.points = points
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
            sum += i*arr2[i]
        return sum

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
            raise ValueError("Determinante de A = 0")

        B = np.dot(Ai, C)

        a, b = B[1], B[0]
        
        return a*self.xp + b
