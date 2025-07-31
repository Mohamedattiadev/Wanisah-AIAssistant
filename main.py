import speech_recognition as sr
import webbrowser
import os
import datetime
import pyttsx3
import subprocess
from gpt4all import GPT4All
import gtts
import subprocess

# --- Initialization ---

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)

# Initialize the offline AI model
# This happens only once when the script starts.
# The first run will download the model file.
print("Loading offline model... This may take a moment.")
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
print("Model loaded successfully.")

# Initialize a list to store the conversation history
chat_history = []


# --- Core Functions ---

def speak(text):
    """Saves speech as an MP3 using Google's online TTS and plays it."""
    print(f"Jarvis: {text}")
    try:
        # Create the TTS object with the text to speak
        tts = gtts.gTTS(text=text, lang="en", slow=False)

        # Save the audio to a file
        tts.save("response.mp3")

        # Use the mpg123 player to play the audio file
        subprocess.run(["mpg123", "-q", "response.mp3"])

    except Exception as e:
        print(f"Error in text-to-speech: {e}")
        # Fallback to the old offline voice if there's an internet issue
        engine.say(text)
        engine.runAndWait()


def takeCommand():
    """Listens for a command and returns it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        # This new line helps calibrate to background noise
        r.adjust_for_ambient_noise(source, duration=1) 
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"You: {query}")
            return query
        except Exception as e:
            print("Sorry, I could not recognize your voice.")
            return ""


def chat(query):
    """Handles conversational chat using the offline GPT4All model."""
    global chat_history

    # Add the user's message to the history
    chat_history.append({'role': 'user', 'content': query})

    print("Generating response from offline model...")
    try:
        response = model.chat_completion(chat_history, streaming=False)
        response_text = response['choices'][0]['message']['content']

        # Add the model's response to the history to maintain context
        chat_history.append({'role': 'assistant', 'content': response_text})

        speak(response_text)
    except Exception as e:
        print(f"Error generating response: {e}")
        speak("I'm sorry, I encountered an error trying to generate a response.")


# --- Main Execution Loop ---

if __name__ == '__main__':
    speak("System online. I am ready to assist you.")

    while True:
        query = takeCommand().lower()

        # --- Pre-defined Commands ---

        # List of websites to open
        sites = [
            ["youtube", "https://www.youtube.com/"],
            ["wikipedia", "https://www.wikipedia.org/"],
            ["google", "https://www.google.com/"]
        ]
        # Loop through the sites to check for "open <sitename>"
        for site in sites:
            if f"open {site[0]}" in query:
                speak(f"Opening {site[0]}, sir.")
                webbrowser.open(site[1])
                # Set query to a consumed state to prevent it falling through to chat()
                query = "command_executed"
                break
        
        if query == "command_executed":
            continue

        # --- Custom Qtile and Rofi Commands ---
        if 'open rofi' in query:
            speak("As you wish.")
            subprocess.run(["rofi", "-show", "drun"])

        elif 'go to workspace' in query:
            workspace = ''.join(filter(str.isdigit, query))
            if workspace:
                speak(f"Switching to workspace {workspace}.")
                subprocess.run(["qtile", "cmd-obj", "-o", "group", "-i", workspace, "-f", "toscreen"])
            else:
                speak("You need to specify a workspace number.")

        # --- Other System Commands ---
        elif "the time" in query:
            strfTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, the time is {strfTime}")

        elif "jarvis quit" in query or "exit" in query:
            speak("Goodbye, sir.")
            exit()

        # --- Conversational Fallback ---
        # If the query is not a pre-defined command and not empty, chat with the AI
        elif query:
            chat(query)
