#text to speech using pyttsx3 lib
import pyttsx3
engine = pyttsx3.init()
text2 = "hello sir, how can i help you"
engine.say(text2)
engine.__reduce__()
text = input(print("enter text :"))
engine.say(text)
engine.runAndWait()