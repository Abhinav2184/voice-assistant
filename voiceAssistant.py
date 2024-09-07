import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def greet():
    print("Hello! how can I help you")
    speak("Hello! how can I help you")

def command():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing.....")
        a=r.recognize_google(audio)
        print("Command: ",a)
        
    except Exception as e:
        print("   speak again")
    return a

if __name__=="__main__" :

    greet()

    while True:

        a=command().lower()

        if 'who' in a:
            a=a.replace("who","")
            results=wikipedia.summary(a)
            print(results)
            speak(results)

        elif 'youtube' in a:
            webbrowser.open("youtube.com")
        
        elif 'google' in a:
            webbrowser.open("google.com")
        
        elif 'open vs code' in a:
            vspath="C:\\Users\\rawat\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vspath)
        
        elif 'play' in a:
            song=a.replace("play","")
            print("Playing...")
            speak("Playing...")
            pywhatkit.playonyt(song)