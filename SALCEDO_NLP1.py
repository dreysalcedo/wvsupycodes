# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 12:42:20 2021

@author: gtxnn
"""


import nltk
from nltk import FreqDist
from nltk.tokenize import word_tokenize

word_data = "Many years ago, there was a kingdom by the sea. In this kingdom lived a young woman called Annabel Lee, whom the speaker suggests the reader might know. According to the narrator, Annabel Lee's only ever thought about the love between them.They were both children, but their love went well beyond what love can normally be. In fact, this love was so special that the angels of heaven were jealous and desirous of it.For that reason, back then, Annabel Lee was killed by wind from a cloud. She was then taken away by people the narrator calls highborn kinsmen, who could be the angels or Annabel Lee's own family members. They enclosed her in a tomb, still within the same kingdom.Retrospectively, the speaker believes that the angels, unhappy in heaven and envious of the love between him and Annabel Lee, caused the wind that killed her.Their love, says the speaker, was more powerful than the love between people older and wiser than them. Furthermore, no angel from heaven or demon under the sea could ever separate his soul from Annabel Lee's.Every time the moon shines, it brings the speaker dreams of his beloved. When the stars rise, he can sense her sparkling eyes. Every night the speaker lies down alongside Annabel Lee—whom he calls his life and bride—in her tomb, with the sound of the sea coming from nearby."
print('WORD DATA::', word_data)
print('=================================================================================================================')
nltk_tokens = nltk.word_tokenize(word_data)
print ('TOKENIZED:', nltk_tokens)
print('=================================================================================================================')
print("Number of words: " , len(word_data))
print('=================================================================================================================')
print("Frequency of word with a plot of words with most repetitions")
freqDist = FreqDist(nltk_tokens)
print(freqDist)
freqDist.plot(10) 
print('=================================================================================================================')
ordered_tokens = set()
result = []
for word in nltk_tokens:
    if word not in ordered_tokens:
        ordered_tokens.add(word)
        result.append(word)
print("Unique words(Filtered duplicate words)")        
print(result)