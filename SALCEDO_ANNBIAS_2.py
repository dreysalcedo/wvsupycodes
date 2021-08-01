# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 02:52:45 2020

@author: gtxnn
"""

import matplotlib.pylab as plt
import numpy as np

def even(x):
    return 2*x
x  = np.arange(-8, 8, 0.1)
f = 1 / (1 + np.exp(-x))
print("Input first weight value: ")
w1 = even(float(input()))
print("Input second weight value: ")
w2 = even(float(input()))
print("Input third weight value: ")
w3 = even(float(input()))
print("Input bias: ")
b = float(input())
l1 = w1
l2 = w2
l3 = w3
for w, l in [(w1, l1), (w2, l2), (w3,l3)]:
    f = 1 / (1 + np.exp(-x*w+b))
    plt.plot(x, f, label=l)          
plt.xlabel('x')
plt.ylabel('h_w(x)')
plt.legend(loc=2)
plt.show()