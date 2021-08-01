# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:43:48 2021

@author: gtxnn
"""

import nltk
from nltk import word_tokenize
import re

#	reads in a text
f = open('corpus.txt')
raw = f.read()


matches = re.findall(r'\b(do)(n\'t)', raw)
print(matches)
