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
    import datetime
    from math import sqrt
    from math import pi
    
    n = [1e2, 1e3, 1e4, 1e5, 1e6, 1e7] #int(input("Give a number of points: "))
    for N in n:
        c = 0
        t0 = datetime.datetime.now()
        for i in range(int(N)):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            if sqrt(x*x + y*y) < 1:
                c += 1
        pi_aprox = 4*c/N
        diff = abs(pi - pi_aprox)
        t1 = datetime.datetime.now()
        print("N = " + str(int(N)) + "; pi ~= " + str(pi_aprox) + 
              "; |pi - pi_aprox| = " + str(diff) + "; time = " + str(t1-t0))
