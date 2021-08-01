# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:49:57 2021

@author: gtxnn
"""

import nltk
from nltk.corpus import genesis

text = genesis.words()
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()


for word in text:
	print(word)
	print("porter: " + porter.stem(word))
	print("lancaster: " + lancaster.stem(word))