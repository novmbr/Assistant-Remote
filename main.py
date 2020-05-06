import requests
import speech_recognition as sr
import json
from playsound import playsound
from gtts import gTTS
import random
import os


def comprehendData(query):
    response = requests.get(f"https://api.novemberai.com/query?q={query}")

    response = json.loads(response.text)['response']
    return response


def recordAudio():
    errorCount = 0
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        voice.speak("I seem to have had a problem.")

    return data


def speak(audioString):
    # MALE

    # engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id)
    # engine.say(audioString)
    # engine.runAndWait()

    # FEMALE

    tts = gTTS(text=audioString, lang='en', )
    randomString = ''.join(random.choice(
        'abdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(16))
    tts.save(f"{randomString}.mp3")
    f = open('log.txt', 'a')
    f.write("Response: " + audioString + "\n")
    playsound(f"{randomString}.mp3")
    os.remove(f"{randomString}.mp3")


while 1:
    data = recordAudio()
    if "November" in data:
        speak(comprehendData(data))
