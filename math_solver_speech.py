import speech_recognition as sr
import wolframalpha
import pyttsx3

recognizer = sr.Recognizer()
recognizer.recognize_google_cloud
mic = sr.Microphone()

with mic as source:
    audio = recognizer.listen(source)

output = recognizer.recognize_google(audio)
print(output)

engine = pyttsx3.init()
client = wolframalpha.Client("3KTG5A-YLKLJPKX9T")

res = client.query(output)
wolfram_res = next(res.results).text

engine.say(wolfram_res)
engine.runAndWait()
