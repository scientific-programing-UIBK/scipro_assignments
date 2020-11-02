#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:27:04 2020
Exercise #04-02: Monte-Carlo estimation of π (Pi)

A simple way to estimate π using a computer is based on a Monte-Carlo method. 
By drawing a sample of N points with random 2D coordinates (x, y) in the 
[0, 1[ range, the ratio of points that fall within the unit circle divided by 
the total number of points (N) gives an estimate of π/4.
Provide two implementations of the monte-carlo estimation of π: a pure python 
version (standard library) and a vectorized version using numpy. Time their 
execution for N = [1e2, 1e3, …, 1e7]. Optional: plot the numpy speed-up as a 
function of N.
Optional: try the numpy version with N=1e8 and above. Make conclusions about a 
new trade-off happening for large values of N.
@author: Francesc Roura Adserias
"""

if __name__ == '__main__':
    # Pure python version (standard library)
    import random
    import datetime #to check time
    from math import sqrt
    from math import pi
    t = [] #initialize time vector
    n = [1e2, 1e3, 1e4, 1e5, 1e6, 1e7] # number of points (n) 
    for N in n:
        c = 0
        t0 = datetime.datetime.now()
        for i in range(int(N)): # create random points in an 1x1 square (1st quadrant)
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            if sqrt(x*x + y*y) < 1: # find if it falls inside the circle
                c += 1
        pi_aprox = 4*c/N
        diff = abs(pi - pi_aprox) #
        t1 = datetime.datetime.now()
        t.append((t1-t0).total_seconds())
        print("N = " + str(int(N)) + "; pi ~= " + str(pi_aprox) + 
              "; |pi - pi_aprox| = " + str(diff) + "; time = " + str((t1-t0).total_seconds()) + 's')
    # import plotting libraries
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.log10(n)
    plt.plot(x, t)

    print("##### USING NUMPY: ######")
    # define sum and multiplication functions
    def multiply_arrays(A, B):
        return np.multiply(A, B)
    def add_arrays(A, B):
        return np.add(A, B)
    n = [1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8] # number of points
    tnum = []
    for N in n:
        c = 0
        t0 = datetime.datetime.now()
        x = np.random.uniform(0, 1, int(N))
        y = np.random.uniform(0, 1, int(N))
        xx = multiply_arrays(x, x)
        yy = multiply_arrays(y, y)
        xxyy = add_arrays(xx, yy)
        c = len([i for i in xxyy if i < 1]) # count points that fall inside the circle
        pi_aprox = 4*c/N
        diff = np.abs(pi - pi_aprox)
        t1 = datetime.datetime.now()
        tnum.append((t1-t0).total_seconds())
        print("N = " + str(int(N)) + "; pi ~= " + str(pi_aprox) + 
                  "; |pi - pi_aprox| = " + str(diff) + "; time = " + str((t1-t0).total_seconds()) + 's')
    # final plot
    x = np.log10(n)
    plt.ylabel('spent time (s)')
    plt.xlabel('log10(iterations)')
    plt.plot(x, tnum)    