import webbrowser
import subprocess
import datetime
from . import system_info 

def handle_command(query, speak):
    """
    Checks for and executes all predefined local and web commands.
    Returns True if a command was handled, False otherwise.
    """
    # --- Web Commands ---
    if "open youtube" in query:
        speak("Opening YouTube, sir.")
        webbrowser.open("https://www.youtube.com/")
        return True
    elif "open google" in query:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
        return True
    elif "search for" in query:
        search_term = query.replace("search for", "").strip()
        if search_term:
            speak(f"Searching the web for {search_term}.")
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
        else:
            speak("What would you like me to search for?")
        return True

    # --- Desktop Commands ---
    elif 'open rofi' in query:
        speak("As you wish.")
        subprocess.run(["rofi", "-show", "drun"])
        return True
    elif 'go to workspace' in query:
        workspace = ''.join(filter(str.isdigit, query))
        if workspace:
            speak(f"Switching to workspace {workspace}.")
            subprocess.run(["qtile", "cmd-obj", "-o", "group", "-i", workspace, "-f", "toscreen"])
        else:
            speak("You need to specify a workspace number.")
        return True
    elif "the time" in query:
        strfTime = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Sir, the time is {strfTime}")
        return True
        
    # --- System Info Commands ---
    elif "cpu usage" in query:
        speak(system_info.get_cpu_usage())
        return True
    elif "memory usage" in query:
        speak(system_info.get_memory_usage())
        return True
        
    # If no command was matched, return False
    return False
