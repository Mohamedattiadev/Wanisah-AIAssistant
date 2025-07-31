import os

TODO_FILE = "todo.txt"

def add_todo(task, speak):
    """Adds a task to the todo.txt file."""
    with open(TODO_FILE, "a") as f:
        f.write(f"{task}\n")
    speak(f"I've added '{task}' to your to-do list.")

def read_todo(speak):
    """Reads all tasks from the todo.txt file."""
    if not os.path.exists(TODO_FILE):
        speak("Your to-do list is empty, sir.")
        return

    with open(TODO_FILE, "r") as f:
        tasks = f.readlines()
        if not tasks:
            speak("Your to-do list is empty, sir.")
            return
            
        speak("Here is what's on your to-do list:")
        for i, task in enumerate(tasks):
            speak(f"Item {i + 1}: {task.strip()}")

def clear_todo(speak):
    """Deletes the todo.txt file."""
    if os.path.exists(TODO_FILE):
        os.remove(TODO_FILE)
        speak("I have cleared your to-do list.")
    else:
        speak("You have no to-do list to clear, sir.")
