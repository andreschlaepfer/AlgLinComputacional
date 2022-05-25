import numpy as np
import matplotlib.pyplot as plt
from math import *
from src.utils.operations import *

class Interpolation:
    def __init__(self, points):
        self.points = points
        self.n = len(self.points)
        self.m = self.n -1
        self.x = [i[0] for i in self.points]
        self.y = [i[1] for i in self.points]
        self.xplt = np.linspace(self.get_x()[0], self.get_x()[-1])
        self.yplt = np.array([], float)
        self.xyplt = self.get_xyplt()
    
    def get_x(self):
        return np.array([i[0] for i in self.points], float)
    def get_y(self):
        return np.array([i[1] for i in self.points], float)
    def get_xyplt(self):
        return [self.xplt, self.yplt]
    

    def get_lagrangian_interpolation_yp_from_xp(self, xp):
        yp = 0
        for i in range(self.n + 1):
            p = 1
            for j in range(self.n + 1):
                if j != i:
                    p *= (xp - self.x[j]) / (self.x[i] - self.x[j])
            yp += self.y[i]*p
        self.points.append([xp, yp])
        return xp, yp
    
    def get_full_lagrangian_interpolation(self):
        for xp in self.xplt:
            yp = 0
            for xi, yi in zip(self.get_x(), self.get_y()):
                yp += yi * np.prod((xp - self.get_x()[self.get_x() != xi]) / (xi - self.get_x()[self.get_x() != xi]))
            self.yplt = np.append(self.yplt, yp)


    def show_graph(self, full = True):
        if (full == False):
            plt.plot(self.get_x, self.get_y, 'ro')
        else:
            plt.plot(self.get_x, self.get_y, 'ro', self.xplt, self.yplt, 'b-')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()