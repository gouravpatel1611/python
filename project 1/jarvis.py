import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("  Good Morning ")
    elif hour >= 12 and 12<18:
        speak("   Good afternoon ")
    else:
        speak("   Good evening ")
    speak( "     I am jarvis and made by Rahul  ")

    
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing ...")
        query = r.recognize_google(audio,language='en-in')
        print("User Sad :- ",query)
    except Exception as e :
        print(e)
        print("say the again plz ")
        return "None"
if __name__ == "__main__":
    wish_me()
    takeCommand()
    