# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 16:23:27 2021

@author: gtxnn
"""
import nltk
from collections import defaultdict
from nltk import FreqDist
from nltk.corpus import wordnet as wn
#1
print("-----------------------------")   
words = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
print("1." , words)
print("1.A. Print all words beginning with sh")
print([w for w in words if w.startswith('sh')])
print("1.B. Print all words longer than four characters ")
print([w for w in words if len(w)>4])
#2
print("-----------------------------")   
entries = nltk.corpus.cmudict.entries()
all_words = [e[0] for e in entries]
distinct_words = set(all_words)
counts = FreqDist(all_words)
polypron_words = [c for c in all_words if counts[c] > 1]
final_fraction = len(polypron_words) / len(distinct_words)
print("2.")
print(" The CMU pronuncing dictionary contains:  %i distinct words" % len(distinct_words))
print("The fraction of words in this dictionary that can have more than one possible pronunciation is ", final_fraction)
#3
print("-----------------------------")   
def similarity(word1, word2):
    synset1 = wn.synset(word1 + '.n.01')
    synset2 = wn.synset(word2 + '.n.01')
    return synset1.path_similarity(synset2)
print("3. ")
print("car-automobile", similarity("car", "automobile"))
print("gem-jewel ", similarity("gem", "jewel"))
print("journey-voyage ", similarity("journey", "voyage"))
print("boy-lad ", similarity("boy", "lad"))
print("coast-shore ", similarity("coast", "shore"))
print("asylum-madhouse ", similarity("asylum", "madhouse"))
print("magician-wizard ", similarity("magician", "wizard"))
print("midday-noon ", similarity("midday", "noon"))
print("furnace-stove  ", similarity("furnace", "stove"))
print("food-fruit ", similarity("food", "fruit"))
print("bird-cock ", similarity("bird", "cock"))
print("bird-crane  ", similarity("bird", "crane"))
print("tool-implement ", similarity("tool", "implement"))
print("brother-monk ", similarity("brother", "monk"))
print("lad-brother ", similarity("lad", "brother"))
print("crane-implement ", similarity("crane", "implement"))
print("journey-car ", similarity("journey", "car"))
print("monk-oracle ", similarity("monk", "oracle"))
print("cemetery-woodland ", similarity("cemetery", "woodland"))
print("food-rooster  ", similarity("food", "rooster"))
print("coast-hill  ", similarity("coast", "hill"))
print("forest-graveyard  ", similarity("forest", "graveyard"))
print("monk-slave  ", similarity("monk", "slave"))
print("coast-forest  ", similarity("coast", "forest"))
print("lad-wizard  ", similarity("lad", "wizard"))
print("chord-smile  ", similarity("chord", "smile"))
print("glass-magician  ", similarity("glass", "magician"))
print("rooster-voyage  ", similarity("rooster", "voyage"))
print("noon-string  ", similarity("noon", "string"))
#4
print("-----------------------------")  
print("4.")
sentence = 'inexpressible'
print("String is", sentence)
print("Substring 'e':", sentence.index('e'))
print("4.A Substring 're':", sentence.index('re'))
print("4.B")
words = ["Hello", "Good", "Morning", "Everyone"]
print("Hello is in position", words.index("Hello"))
print("Good is in position", words.index("Good"))
print("Morning is in position", words.index("Morning"))
print("Everyone is in position", words.index("Everyone"))

