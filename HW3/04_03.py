#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:25:31 2020
Write a function which converts binary strings to decimal numbers. The 
function should handle unsigned (positive) numbers only.

@author: francesc
"""
if __name__ == '__main__':

    def binary_to_decimal(in_num):
        import sys
        if len(in_num) != 32:
            sys.exit("Number length is not equal to 32")
        #find the position of the point:
        b1 = int(in_num[0])*2**4 
        b2 = int(in_num[1])*2**3
        b3 = int(in_num[2])*2**2
        b4 = int(in_num[3])*2**1
        b5 = int(in_num[4])*2**0
        dec_pos = b1 + b2 + b3 + b4 + b5 
        in_num_5 = in_num[5:]
        bbef = in_num_5[:dec_pos]
        baft = in_num_5[dec_pos:]
        
        dbef = 0
        for i in list(range(0,len(bbef))):
            dbef = dbef + int(bbef[i])*2**(len(bbef)-(i+1))
        
        daft = 0
        for i in list(range(0,len(baft))):
            daft = daft + int(baft[i])*2**-(i+1)
        dfin = dbef + daft
        return(dfin)
        
#    in_num = input("input a binary number: ")

#    dfin = binary_to_decimal(in_num)
#    print("The decimal number is: " + str(dfin))

# what is the smallest number the BSE can represent? The largest?

# The smallest is "00000000000000000000000000000001" (apart from 0)
min = binary_to_decimal("00000000000000000000000000000001")
print("The minimum value is: " + str(min))

# The largest is "1111111111111111111111111111" with prefix (11111=31) until (11011=27)
l1 = binary_to_decimal("11111111111111111111111111111111")
l2 = binary_to_decimal("11110111111111111111111111111111")
l3 = binary_to_decimal("11101111111111111111111111111111")
l4 = binary_to_decimal("11100111111111111111111111111111")
l5 = binary_to_decimal("11011111111111111111111111111111")
print("The larger number is " + str(l1))
print("The larger number is " + str(l2))
print("The larger number is " + str(l3))
print("The larger number is " + str(l4))
print("The larger number is " + str(l5))

# what is the maximal accuracy of the BSE? (in other words, what is the 
# difference between the smallest positive number and zero?)
#The difference between the smallest positive number and zero is:
accu = abs(0-float(binary_to_decimal("00000000000000000000000000000001")))
print("The highest accuracy is: " + str(accu))

# what is the lowest accuracy of our standard? (in other words, what is the 
# difference between the largest number we can represent and the second largest?)
max1 = float(binary_to_decimal("11111111111111111111111111111111"))
max2 = float(binary_to_decimal("11111111111111111111111111111110"))
laccu = abs(max1 - max2)
print("The lowest accuracy of our standard is: " + str(laccu))

# does the difference between two nearest representable change, when the dot 
# position doesn’t?
# -> No, because the last bit (0 or 1) at the last position will be always multiplied by the same exponent.

# now compute the precision of our format for a range of possible values of the 
# BSE for these values, compare the BSE to the IEEE754 binary32 format (or its 
# numpy equivalent np.float32) using numpy.nextafter.
import random
import numpy as np

num=[]
dif=[]
for i in range(1):#range(100000):
    ran = ''
    for i in range(31):
        k = random.randint(0, 1) # decide on a k each time the loop runs
        ran += str(k)
    ran1 = binary_to_decimal(ran + '1')
    ran2 = binary_to_decimal(ran + '0')
    precisionBSE = ran1 - ran2
    
    precisionIEEE754 = np.nextafter(np.float32(ran1),-np.inf) - ran1
    diff = precisionBSE - abs(precisionIEEE754)
    if diff < 0:
        print("BSE is more precise by:")
    else:
        print("IEEE754 is more precise by:")
    dif.append(diff)
    num.append(ran1)
    print(diff)

# import library to plot results
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#import matplotlib.pyplot
#plt.ylabel("precision BSE - precision IEEE754")
#plt.xlabel("log10(float value)")
#plt.title("1e5 points")
#plt.scatter(np.log10(num), dif)

# (optional: you can also use matplotlib and a log-log plot to produce a 
# graphic similar to the wikipedia page on IEEE 754)
x = []
precision = []
for i in range(300):
    x.append(np.log10(10**(-12+i/10)))
    precision.append(np.log10(abs(np.nextafter(np.float32(10**(-12+i/10)), 0) - 10**(-12+i/10))))
plt.ylabel("log10(floating point precision)")
plt.xlabel("log10(floating point value)")
plt.plot(x, precision)
