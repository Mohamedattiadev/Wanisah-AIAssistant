import google.generativeai as genai
from gpt4all import GPT4All
from config.keys import gemini_api_key

def initialize_offline_model():
    """Initializes and returns the GPT4All offline model."""
    print("Loading offline AI model...")
    model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf", device='cpu')
    print("Offline AI model loaded.")
    return model

def initialize_online_model(system_prompt):
    """Initializes and returns the Gemini online model and chat session."""
    print("Configuring online AI model...")
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat_session = model.start_chat(history=[
        {'role': 'user', 'parts': [system_prompt]},
        {'role': 'model', 'parts': ["Understood. I will be direct and efficient."]}
    ])
    print("Online AI model configured.")
    return model, chat_session
