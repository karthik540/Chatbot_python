import speech_recognition as sr

def SpeechRecognizer():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
        except:
            text = 'Audio not Recognizable !'
    
    return text