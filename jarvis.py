#Creating a voice recognition device in python

#Importing important libraries
import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os

#Voice recognition
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning!")
    elif(hour>=12 and hour<18):
        speak("Good afternoon!")
    else:
        speak("Good Evening!")
    speak("Hi! Jarvis here. Please tell me how i may help you")
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return ("None")
    return query


if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query =takeCommand().lower()

        if ("wikipedia" in query):
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif("open youtube" in query):
            webbrowser.open("youtube.com")
        elif ("open google" in query):
            webbrowser.open("google.com")
        elif ("time" in query):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif ("open zoom" in query):
            codePath = "C:\\Users\\user\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(codePath)

        elif("quit" in query):
            exit()

