
import nltk
from nltk.tag import pos_tag, map_tag

#first sentence
print('First Sentence: "I need a flight from Atlanta."')
print('=================================================================')
text = nltk.word_tokenize("I need a flight from Atlanta.")
print(nltk.pos_tag(text))
print('=================================================================')

#map tags for simplification
posTagged = pos_tag(text)
simplifiedTags = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in posTagged]
print(simplifiedTags)
print('=================================================================')


#second sentence
print('Second Sentence: "Can you list the nonstop afternoon flights?"')
print('=================================================================')
text = nltk.word_tokenize("Can you list the nonstop afternoon flights?")
print(nltk.pos_tag(text))
print('=================================================================')

#map tags for simplification
posTagged = pos_tag(text)
simplifiedTags = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in posTagged]
print(simplifiedTags)
print('=================================================================')