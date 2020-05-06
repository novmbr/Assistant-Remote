import requests
import json
import recognition
import speak
import os


def getResponse(query):
    response = requests.get(f"https://api.novemberai.com/query?q={query}")

    response = json.loads(response.text)
    return response


while 1:
    data = recognition.recordAudio()
    response = getResponse(data)

    if "November" in data:
        speak.say(response['response'])
