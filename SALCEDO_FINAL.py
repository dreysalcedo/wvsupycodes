# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 17:03:14 2021

@author: gtxnn
"""
#finals project voice recognition sentiment analysis
#Speech Recognition
import speech_recognition as sr
import pyttsx3
import pyaudio
#SentimentAnalysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
#speech recognition
r = sr.Recognizer()
engine = pyttsx3.init()
      
with sr.Microphone() as source:
    engine.say("Speak Now")
    print("Speak Now: ")
    engine.runAndWait()
    r.pause_threshold = 1
    r.energy_threshold = 6000
    audio = r.listen(source)
#voice
try:
    text = str(r.recognize_google(audio, language="en-US")).lower()
    print(text)
except Exception as ex:
    print(ex)
#Sentiment analysis
print("vaderSentiment")
Sentence=[text]
analyser=SentimentIntensityAnalyzer()
for i in Sentence:
    v = analyser.polarity_scores(i)
    print(v)

print("Textblob")
test = TextBlob(text)
print(test.sentiment)
