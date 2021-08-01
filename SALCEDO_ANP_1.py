# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 02:11:07 2020

@author: gtxnn
"""

import matplotlib.pylab as plt
import numpy as np

x  = np.arange(-8, 8, 0.1)
f = 1 / (1 + np.exp(-x))
print("Input first weight value: ")
w1 = int(input())
print("Input second weight value: ")
w2 = int(input())
print("Input third weight value: ")
w3 = int(input())
l1 = w1
l2 = w2
l3 = w3
for w, l in [(w1, l1), (w2, l2), (w3,l3)]:
    f = 1 / (1 + np.exp(-x*w))
    plt.plot(x, f, label=l)
plt.xlabel('x')
plt.ylabel('h_w(x)')
plt.legend(loc=2)
plt.show()
