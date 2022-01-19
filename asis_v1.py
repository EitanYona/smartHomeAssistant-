# pylint: disable=bad-indentation
from math import trunc
import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
import webbrowser # open browser
import ssl
import certifi
import time
import os # to remove created audio files
import subprocess
import pyttsx3
import urllib.request
import requests

class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name



def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def there_exists_1(terms,voice_data_1):
    for term in terms:
        if term in voice_data_1:
            return True

def there_exists_ac(terms,voice_data_ac):
    for term in terms:
        if term in voice_data_ac:
            return True

def there_exists_emergency(terms,voice_data_emergency):
    for term in terms:
        if term in voice_data_emergency:
            return True
            

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            engine_speak('I did not get that eitan')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()

def record_audio_for_lights(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            engine_speak('I did not get that eitan')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()

def record_audio_for_emergency(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            engine_speak('I did not get that eitan')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()

def record_audio_for_temp(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            engine_speak('I did not get that eitan')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(asis_obj.name + ":", audio_string) # print what app said
    os.remove(audio_file) # remove audio file

def respond(voice_data,light_status,ac_status,ac_deg):
    # 1: greeting
    if there_exists(['hey','hi','hello']):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):

        if person_obj.name:
            engine_speak(f"My name is {asis_obj.name}, {person_obj.name}") #gets users name from voice input
        else:
            engine_speak(f"My name is {asis_obj.name}. what's your name?") #incase you haven't provided your name.

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name) # remember name in person object
    
    if there_exists(["what is my name"]):
        engine_speak("Your name must be " + person_obj.name)
    
    if there_exists(["your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name) # remember name in asis object

    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)
    
    if there_exists(["weather"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")

    #turn on the lights in your home
    if there_exists(["dark","turn on the lights"]):
        if light_status[0] == True:
            engine_speak("Hi I wish I can do better for you, but the lights are already tuerned on")
        if light_status[0] == False:
            voice_data_1 = record_audio_for_lights("Would you like me to turn on the lights?")
            if there_exists_1(["yes"],voice_data_1):
                 url = "https://giphy.com/gifs/CMNHospitals-happy-reaction-girl-IzigK4GlBmchkTqIrG"
                 webbrowser.get().open(url)  
                 engine_speak("I will turn on the lights") 
                 engine_speak("The lights turned on")
                 light_status[0] = True;

    if there_exists(["turn off the lights","lighs off"]):
        if light_status[0] == False:
            engine_speak("the lights already turned off, i suggest that you will closethe shutters")
        if light_status[0] == True:
            engine_speak("No problem I will turn off the lights")
            light_status[0] = False
            engine_speak("lights turned off")
    
    #tempature sensor
    if there_exists(["hot","set the ac temperature","temperature", "cold", 
                     "turn on the ac", "freez","freezing","chill", "chilly",
                     "shivery","shiver","shivering"]):
        if ac_status[0] == True:
            engine_speak("I see that the A C is already working")
            voice_data_ac = record_audio_for_lights("Would you like the set the A C for different temperature")
            if there_exists_ac(["yes"],voice_data_ac):
                 voice_data_ac = record_audio_for_lights("How many degrees would you like?")
                 ac_deg[0] = voice_data_ac;
                 engine_speak("The temperature was set to " + ac_deg[0] + " degrees")
        if ac_status[0] == False:
            voice_data_1 = record_audio_for_lights("Would you like me to turn on the A C?")
            if there_exists_1(["yes"],voice_data_1):
                 engine_speak("The A C turned on")
                 engine_speak("Let's set the temperature")
                 voice_data_1 = record_audio_for_lights("How many degrees would you like?")
                 ac_deg[0] = voice_data_1;
                 engine_speak("The temperature was set to " + ac_deg[0] + " degrees")
                 ac_status[0] = True

    if there_exists(["turn off the ac","ac off"]):
        if ac_status[0] == False:
            engine_speak("the ac already turned off")
        if ac_status[0] == True:
            engine_speak("No problem I will turn off the ac")
            ac_status[0] = False
            engine_speak("ac turned off")

    if there_exists(["home status", "what is the home status"]):
        if ac_status[0] == True:
            engine_speak("The ac is on")
        if ac_status[0] == False:
            engine_speak("The ac is off")
        if light_status[0] == True:
            engine_speak("The lights are on")
        if light_status[0] == False:
            engine_speak("The lights are off")

    if there_exists(["emergency", "i fall", "i am not feeling well"]):
        engine_speak("are you ok?")
        voice_data_emergency = record_audio_for_emergency("would you like me to call someone?")
        if there_exists_emergency(["yes"],voice_data_emergency):
            voice_data_emergency = record_audio_for_emergency("would you like me to call your safety contact or ambulance?")
            if there_exists_emergency(["safety contact"],voice_data_emergency):
                engine_speak("ok i'm calling safety contact")
            if there_exists_emergency(["ambulance"],voice_data_emergency):
                engine_speak("ok i'm calling 9 1 1")
                engine_speak("i'm sending your location as well")
                url = "https://www.google.com/maps/search/Where+am+I+?/"
                webbrowser.get().open(url)   

    

    if there_exists(["exit", "quit", "goodbye"]):
        engine_speak("bye")
        exit()


time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'kiki'
person_obj.name = ""
light_flag_container = [False]
tempatue_container_status = [False] 
tempatue_container_deg = [25]
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("Recording") # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data,light_flag_container,tempatue_container_status,tempatue_container_deg) # respond
