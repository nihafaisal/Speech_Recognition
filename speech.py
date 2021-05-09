import speech_recognition as sr
import random

r = sr.Recognizer()
words = ['hello', 'yes', 'no', 'fire', 'fighter', 'house', 'people', 'name', 'my', 'bluetooth', 'manage', 'person', 'cute', 'terrible', 'building', 'apple', 'seminar', 'kitchen', 'food', 'robot']
phrase =  words[random.randint(0,len(words)-1)] + ' ' + words[random.randint(0,len(words)-1)] + ' ' + words[random.randint(0,len(words)-1)]

with sr.Microphone() as source:
    print("Please say the phrase: " , phrase)
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        detected = "{}".format(text)
        print("you said: ", detected)
    except:
        print("sorry could not recognize your voice")
    
if phrase == detected:
    print("Verrified!")
else:
    print('Try Again')
