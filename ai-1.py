import pyttsx3
import speech_recognition as sr
import openai

recognizer = sr.Recognizer()
microphone = sr.Microphone()

engine = pyttsx3.init()

def record_audio():
    with microphone as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio

#main loop
if __name__ == "__main__":
    while True:
        try:
            audio_input = record_audio()
            text_input = recognizer.recognize_google(audio_input)
            print("You said:", text_input)
            engine.say("You said: " + text_input)
            engine.runAndWait()

            if "hey pluto" in text_input.lower():
                print("Yeah, I'm Pluto. How can I help you?")
                engine.say("Yeah, I'm Pluto. How can I help you?")
                engine.runAndWait()
            elif "who are you" in text_input.lower():
                print("I am an AI assistant.")
                engine.say("I am an AI assistant.craeted by vivek rao for his enjoyment")
                engine.runAndWait()
            elif "who is your creator" in text_input.lower():
                print("vivek rao")
                engine.say("iam craeted by vivek rao")
                engine.runAndWait()
            elif "who created you" in text_input.lower():
                print("I was created by vivek.")
                engine.say("I was created by vivek.")
                engine.runAndWait()
            elif "who is Rohit Sharma" in text_input.lower():
                engine.say("GOAT")
                engine.runAndWait()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            engine.say("Sorry, I couldn't understand what you said.")
            engine.runAndWait()
        except sr.RequestError:
            print("There was an error with the speech recognition service.")
            engine.say("There was an error with the speech recognition service.")
            engine.runAndWait()
