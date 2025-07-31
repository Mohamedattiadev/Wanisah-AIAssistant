# ==============================================================================
# Wanisah AI Assistant - Final Version
# ==============================================================================

# --- Standard Library Imports ---
import os
import sys
import json
import subprocess
import time
import pyttsx3
import gtts
import pyaudio
import vosk
import google.generativeai as genai
from gpt4all import GPT4All
from config.keys import gemini_api_key
from tools import email_service, todo_service, local_commands, weather, calculator
from google.api_core import exceptions
from config.startup import display_banner
from config.persona import system_prompt

# ==============================================================================
# SUPPRESS STARTUP LOGS & DISPLAY BANNER
# ==============================================================================

# Redirect stderr to hide verbose startup logs
original_stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')

display_banner()

# ==============================================================================
# INITIALIZATION
# ==============================================================================

# --- Text-to-Speech Engine (for fallback) ---
offline_engine = pyttsx3.init()
offline_engine.setProperty('rate', 175) 

# --- Offline Speech-to-Text (Vosk) ---
VOSK_MODEL_PATH = "vosk-model"
if not os.path.exists(VOSK_MODEL_PATH):
    raise FileNotFoundError("Vosk model not found. Please download and place it in the 'vosk-model' directory.")
vosk_model = vosk.Model(VOSK_MODEL_PATH)
vosk_recognizer = vosk.KaldiRecognizer(vosk_model, 16000)
mic = pyaudio.PyAudio()

# --- Offline AI Model (for on-demand use) ---
print("Loading offline AI model...")
offline_model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf", device='cpu')
print("Offline AI model loaded.")

# --- Online AI Model (for general conversation) ---
genai.configure(api_key=gemini_api_key)
gemini_model = genai.GenerativeModel('gemini-2.5-flash')
chat_session = gemini_model.start_chat(history=[
    {'role': 'user', 'parts': [system_prompt]},
    {'role': 'model', 'parts': ["Understood. I will be direct and efficient."]}
])

# Restore stderr so we can see runtime errors
sys.stderr = original_stderr
print("All models loaded successfully.")


# ==============================================================================
# CORE FUNCTIONS
# ==============================================================================

def speak(text):
    """Saves speech, speeds it up with FFmpeg, and then plays it."""
    print(f"Wanisah: {text}")
    try:
        tts = gtts.gTTS(text=text, lang="en", slow=False)
        tts.save("response_normal.mp3")
        subprocess.run(
            ["ffmpeg", "-i", "response_normal.mp3", "-filter:a", "atempo=1.4", "-vn", "response_fast.mp3", "-y"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        subprocess.run(["mpg123", "-q", "response_fast.mp3"])
    except Exception as e:
        print(f"Online TTS failed: {e}. Falling back to offline voice.")
        offline_engine.say(text)
        offline_engine.runAndWait()


def takeCommand():
    """Listens for a command using the fast offline Vosk engine."""
    vosk_recognizer = vosk.KaldiRecognizer(vosk_model, 16000)
    
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4096)
    print("Listening...")
    stream.start_stream()
    
    start_time = time.time()
    
    try:
        while time.time() - start_time < 15: # 15 second timeout
            data = stream.read(4096, exception_on_overflow=False)
            if vosk_recognizer.AcceptWaveform(data):
                result = json.loads(vosk_recognizer.Result())
                query = result.get("text", "")
                if query:
                    print(f"You: {query}")
                    return query
    except Exception as e:
        print(f"Error during recognition: {e}")
    finally:
        stream.stop_stream()
        stream.close()
        
    print("Listening timed out.")
    return ""


def chat_online(query):
    """Handles conversational chat using a response from Gemini."""
    print("Sending to Gemini for a smart response...")
    try:
        response = chat_session.send_message(query)
        speak(response.text.strip())
    except exceptions.ResourceExhausted as e:
        print(f"Gemini quota exceeded: {e}. Falling back to offline model.")
        chat_offline(query)
    except Exception as e:
        print(f"Error communicating with Gemini: {e}")
        speak("I'm sorry, sir. I'm having trouble connecting to the online AI service.")


def chat_offline(query):
    """Handles conversational chat using the local GPT4All model."""
    prompt = f"User: {query}\nAssistant:"
    print("Generating response from offline model...")
    try:
        response = offline_model.generate(prompt, max_tokens=100)
        speak(response.strip())
    except Exception as e:
        print(f"Error with offline model: {e}")
        speak("I'm sorry, I encountered an error with the local model.")


# ==============================================================================
# MAIN EXECUTION LOOP
# ==============================================================================

if __name__ == '__main__':
    speak("System online. I am ready to assist you.")
    while True:
        query = takeCommand().lower()
        if not query:
            continue

        # --- Strict Offline-First Router ---
        if local_commands.handle_command(query, speak):
            continue
        elif "weather in" in query:
            city = query.replace("weather in", "").strip()
            weather.get_weather(city, speak)
        elif "calculate" in query or ("what is" in query and any(c in query for c in "+-*/")):
            result = calculator.calculate(query)
            speak(result)
        elif "send an email" in query:
            email_service.send_email_flow(speak, takeCommand)
        elif "add" in query and "to my to-do list" in query:
            task = query.replace("add", "").replace("to my to-do list", "").strip()
            if task: 
                todo_service.add_todo(task, speak)
        elif "what's on my to-do list" in query or "read my to-do list" in query:
            todo_service.read_todo(speak)
        elif "clear my to-do list" in query:
            todo_service.clear_todo(speak)
        elif "ask the local model" in query or "using offline ai" in query:
            prompt = query.replace("ask the local model", "").replace("using offline ai", "").strip()
            chat_offline(prompt)
        elif "jarvis quit" in query or "wanisah quit" in query or "exit" in query:
            speak("Goodbye, sir.")
            exit()
        else:
            chat_online(query)
