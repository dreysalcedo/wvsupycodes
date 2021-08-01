

import nltk
from nltk.tag import pos_tag, map_tag

print('The Sentence: "We may also collect information you voluntarily add to your profile, such as your mobile phone number and mobile service provider."')
print('=================================================================')
text = nltk.word_tokenize('We may also collect information you voluntarily add to your profile, such as your mobile phone number and mobile service provider.')
print(nltk.pos_tag(text))
print('=================================================================')

#map tags for simplification
posTagged = pos_tag(text)
simplifiedTags = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in posTagged]
print(simplifiedTags)

print('=================================================================')