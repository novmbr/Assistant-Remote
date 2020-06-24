from playsound import playsound
import random
import os
import requests


def say(audioString):
    randomString = ''.join(random.choice(
        'abdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(16))
    with open(f'voice/{randomString}.mp3', 'wb') as f:
        f.write(requests.get(
            "https://api.novemberai.com/voice?t=" + audioString).content)
    playsound(f"voice/{randomString}.mp3")
    os.remove(f"voice/{randomString}.mp3")
