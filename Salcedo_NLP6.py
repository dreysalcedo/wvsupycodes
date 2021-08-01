# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:15:38 2021

@author: gtxnn
"""

string = "themartian"
dictionary = ['the', 'martian', ]

def max_match(sentence, dictionary):
    if not sentence:
        return ""
    for i in range(len(sentence), -1, -1):
        first_word = sentence[:i]
        remainder = sentence[i:]
        if first_word in dictionary:
            return first_word + " " + max_match(remainder, dictionary)
    first_word = sentence[0]
    remainder = sentence[1:]
    return first_word + max_match(remainder, dictionary)
print(max_match(string, dictionary))