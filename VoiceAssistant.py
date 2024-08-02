import speech_recognition as sr # type: ignore
import pyttsx3 # type: ignore
from datetime import datetime
import webbrowser
voice_recognizer = sr.Recognizer()
text_to_speech_engine = pyttsx3.init()
def speak(output_text):
    text_to_speech_engine.say(output_text)
    text_to_speech_engine.runAndWait()
def listen():
    with sr.Microphone() as audio_source:
        print("Listening...")
        audio_data = voice_recognizer.listen(audio_source)
        try:
            recognized_text = voice_recognizer.recognize_google(audio_data)
            print(f"You said: {recognized_text}")
            return recognized_text.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""
def process_command(user_command):
    if "hello" in user_command:
        speak("Hello! How can I assist you today?")
    elif "time" in user_command:
        current_time = datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif "date" in user_command:
        current_date = datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif "search" in user_command:
        speak("What would you like to search for?")
        search_query = listen()
        if search_query:
            search_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(search_url)
            speak(f"Here are the results for {search_query}")
    else:
        speak("Sorry, I don't understand that command.")
def main():
    speak("Voice Assistant is now active. How can I help you?")
    while True:
        user_command = listen()
        if "exit" in user_command or "quit" in user_command:
            speak("Goodbye!")
            break
        process_command(user_command)

if __name__ == "__main__":
    main()
