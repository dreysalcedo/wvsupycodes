# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 11:04:46 2020

@author: gtxnn
"""
import matplotlib.pylab as plt
import numpy as np

def odd(x):
    return 2*x+1
print("Input first weight value: ")
w1 = odd(float(input()))
print("Input second weight value: ")
w2 = odd(float(input()))
print("Input third weight value: ")
w3 = odd(float(input()))
l1 = w1
l2 = w2
l3 = w3
x  = np.arange(-8, 8, 0.1)
f = 1 / (1 + np.exp(-x))
for w, l in [(w1, l1), (w2, l2), (w3,l3)]:
    f = 1 / (1 + np.exp(-x*w))
    plt.plot(x, f, label=l)
plt.xlabel('x')
plt.ylabel('f_w(x)')
plt.legend(loc=2)
plt.show()

