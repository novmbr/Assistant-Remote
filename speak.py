from playsound import playsound
from gtts import gTTS
import random
import os


def say(audioString):
    tts = gTTS(text=audioString, lang='en', )
    randomString = ''.join(random.choice(
        'abdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(16))
    tts.save(f"{randomString}.mp3")
    playsound(f"{randomString}.mp3")
    os.remove(f"{randomString}.mp3")
