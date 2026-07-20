import speech_recognition as sr
import webbrowser
import pyttsx3
import pocketsphinx
import MusicLibrary
import requests
import time
from openai import OpenAI
from gtts import gTTS
import pygame
import os


recognizer=sr.Recognizer()
engine = pyttsx3.init()
newsapi="apikey"

def speak(text):
    print("Speaking:",text)
    engine = pyttsx3.init() 
    engine.say(text)
    engine.runAndWait()
    engine.stop()
   
def speak_paid(text): 
    tts = gTTS(text)
    tts.save('text.mp3')

    pygame.mixer.init()
    
    pygame.mixer.music.load('text.mp3')
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove('text.mp3')
    
def aiProcess(command):
    client = OpenAI(api_key="")
    response = client.responses.create(
        model="gpt-5.6",
        tools=[{"type": "web_search"}],
        input="What was a positive news story from today"
    )
    return response.output_text.input.content

music = {
    "ishq": "https://www.youtube.com/watch?v=IJeSR-LJBnk",
    "sitara": "https://youtu.be/3_Y885eZ4Es?si=Ii-bZFpY8RsdI36p",
    "karam": "https://www.youtube.com/watch?v=__bHEfJ29j0",
    "parda": "https://www.youtube.com/watch?v=0A1sazs2F5I"
}
  
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")   
        
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        songs=music[song]
        webbrowser.open(songs)
        
        
    elif "news" in c.lower():
        print("News command detected")
        speak("Fetching news")
        time.sleep(2)
        url = f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={newsapi}"
        r = requests.get(url)
        news = r.json() 
        if news["status"] == "ok":
            articles = news["articles"]
 
            for i, article in enumerate(articles, start=1):
                headline = article["title"]
                print(f"{i}. {headline}")
                speak(headline)  
                time.sleep(1) 
        else:
            speak("Sorry, I could not fetch the news.")
            print(news)
    else:
        output=aiProcess(c)
        speak(output)
        
if __name__=="__main__":
    speak("Initializing Jarvis.....")
   
    while True: 
#listening to a wake word "Jarvis"
#obtained audio from the microphone
        r = sr.Recognizer()
        
        print("Recognize...")
        try:
        # recognize speech using Sphinx
            with sr.Microphone() as source:    
                print("Listening....")
                # Listening for command 
                audio = r.listen(source,timeout=3,phrase_time_limit=3 )
                word= r.recognize_google(audio)
                print(word)
                
            if word.lower()=="jarvis":
                speak("ya")
                    
                with sr.Microphone() as source:    
                    print("jarvis Active")
                    audio = r.listen(source,timeout=3, phrase_time_limit=3 )
                    command= r.recognize_google(audio)
                    print(command)
                processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

