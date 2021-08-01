# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 17:03:14 2021

@author: gtxnn
"""

import speech_recognition as sr
import pyttsx3
import pyaudio
import webbrowser
r = sr.Recognizer()
from datetime import datetime

now = datetime.now().time() # time object



engine = pyttsx3.init()

      
with sr.Microphone() as source:
    engine.say("Speak Now")
    print("Speak Now: ", "Current Time =", now)
    engine.runAndWait()
    r.pause_threshold = 1
    r.energy_threshold = 6000
    audio = r.listen(source)

try:
    text = str(r.recognize_google(audio, language="fil-PH")).lower()
    print(text)
    
    with open('sample.txt', 'w') as f:  
        f.write(text)
       

except:
    print("END")
pass

f.close()