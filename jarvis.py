# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 23:21:32 2019

@author: gtxnn
"""

import numpy as np
from math import sqrt
import pyttsx3#pip install pyttsx3   text to speech conversion module available offline
import speech_recognition as sr #pip install SpeechRecognition  speech recognition module
import datetime #get time 
import wikipedia #pip install wikipedia                 access wikepedia
import webbrowser#pip install webbrowser                access web browser
import os                                               #open/save files
import smtplib #pip install smtplib                     module used to send mail 
import re
import requests #pipenv install requests
import sys
import time
import playsound #pip install playsound                module to enable play saved mp3 files
from gtts import gTTS #pip install gTTS                text to speech module by google
import random
import subprocess #pip install subprocess.run 
from bs4 import BeautifulSoup as soup # pip install beautifulsoup4
from urllib.request import urlopen # pip install urllib
import pyowm #pip install pyowm                            module for weather
import wolframalpha #pip install wolframalpha              module to calculate
#-------------------------------



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()  
              
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Madam!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Madam!")   

    else:
        speak("Good Evening Madam!")  

    speak("I am Molly. Please tell me how may I help you")   
wishMe()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something.")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")   
        speak("recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Can't recognize...")  
        speak("Can't recognize...")  
       
        return "None"
    return query
   
     
       
def assistant(query):
        #ga error
        # Logic for executing tasks based on query
        if 'email' in query:   
            try:
                speak('What should i say')
                content = takeCommand()
                #init gmail smtp
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                #identify to server
                mail.ehlo()
                #encrypt session
                mail.starttls()
                #login
                mail.login('recabarbm@gmail.com', 'recabarbeamerr05')
                #send message
                mail.sendmail('Bea Merr Recaabr', 'beamerr.recabar@wvsu.edu.ph', content)
                #close
                mail.close                
                #email sent
                speak('email sent')
                
            except:
                speak('Sorry Madam! I am unable to send your message at this moment!')    
             
              
        elif 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)    
            except:
                speak('Im sory madam! i am unable to perform this task at this moment')
               
        elif "chrome" in query: 
            speak("Google Chrome") 
            os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')  
             
        elif 'hello' in query:          
            speak('Hello Madam')             
        
        elif 'Molly are you there' in query:
            speak('always at your service')
             
        elif 'what is your name' in query:
            speak('Im Molly, Madam')
             
        elif 'introduce yourself' in query:
            speak('Allow me to introduce myself. I am Molly, a virtual Artificial Intelligence. I am here to assist you with a variety of task as best as i can, 24 hours a day, 7 days a week.')
            
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Madam")
        
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/ maps / place/" + location + "/&amp;")
            speak('hr')
        
        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Bea.")
        
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
        
        elif 'open youtube' in query or 'youtube' in query or 'visit youtube' in query or 'go to instagram' in query :
            webbrowser.open("youtube.com")
            speak('opening youtube')

        elif 'open google' in query or 'google' in query or 'visit google' in query or 'go to instagram' in query :
            webbrowser.open("google.com")
            speak('opening google')

        elif 'open facebook' in query or 'facebook' in query or 'visit facebook' in query or 'go to instagram' in query :
            webbrowser.open("facebook.com") 
            speak('opening facebook')
            
        elif 'Open instagram' in query or 'instagram' in query or 'go to instagram' in query or 'visit instagram' in query:
            webbrowser.open("instagram.com")   
            speak('opening instagram')

        elif 'what time is it' in query or 'time' in query or 'time check' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Madam, the time is {strTime}")            
        
        elif 'open notepad' in query or 'notepad' in query:
            os.startfile('notepad.exe')    
      
        elif 'news for today' in query or 'news' in query:
            try:
                news_url="https://news.google.com/news/rss"
                Client=urlopen(news_url)
                xml_page=Client.read()
                Client.close()
                soup_page=soup(xml_page,"xml")
                news_list=soup_page.findAll("item")
                for news in news_list[:15]:
                    speak(news.title.text.encode('utf-8'))
            except Exception as e:
                print(e)
        
        elif "calculate" in query: 
              
            # write your wolframalpha app_id here 
            app_id = "5XTUEJ-4UEY85L6VJ" 
            client = wolframalpha.Client(app_id) 
  
            indx = query.lower().split().index('calculate') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            print("The answer is " + answer)
            speak("The answer is " + answer)
               
                
        elif 'nothing' in query or 'end' in query or 'abort' or 'nothing else' in query or 'stop'  in query or 'Goobye' in query or 'Goobye Jarvis' in query:            
            speak('Bye Madam, have a good day.')
            sys.exit()
        
#loop to continue executing multiple commands
while True:
    assistant(takeCommand())
    speak('What is your next command') 
 