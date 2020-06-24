import requests
import json
import recognition
import speak
import os


def getResponse(query):
    response = requests.get(f"https://api.novemberai.com/query?q={query}")

    response = json.loads(response.text)
    return response


def start():
    print("Listening...")
    data = recognition.recordAudio()
    response = getResponse(data)
    print(f"Listened. Got \"{data}\"")

    speak.say(response['response'])
