import speech_recognition as sr


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
