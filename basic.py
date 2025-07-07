import pyttsx3
import speech_recognition as sr

# Initialize speech recognition and text-to-speech engine
recognizer = sr.Recognizer()
microphone = sr.Microphone()
engine = pyttsx3.init()

# Predefined phrases
phrases = ["hey pluto", "who are you", "what is your"]
phrases_additional = ["had breakfast", "had dinner", "had lunch", "who created you"]

# Function to record audio from microphone
def record_audio():
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)       
    return audio

# Function to process recognized text
def process_input(text_input):
    text_input = text_input.lower()

    if text_input in phrases:
        response = "Yeah, I'm Pluto. How can I help you?"
    elif text_input in phrases_additional:
        if text_input == "who created you":
            response = "Yeah, I'm Sravani's pet. He created me for his enjoyment."
        else:
            response = "I am an AI, I can't even eat. Well, what about your meal?"
    else:
        response = "I'm not sure how to respond to that."

    print(response)
    engine.say(response)
    engine.runAndWait()

# Main function
if __name__ == "__main__":
    try:
        audio_input = record_audio()
        text_input = recognizer.recognize_google(audio_input)
        print("You said:", text_input)
        process_input(text_input)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        engine.say("Sorry, I couldn't understand what you said.")
        engine.runAndWait()
    except sr.RequestError as e:
        print(f"There was an error with the speech recognition service: {e}")
        engine.say("There was an error with the speech recognition service.")
        engine.runAndWait()

