````markdown
# Wanisah AI Assistant

<p align="center">
  <img src="https://img.icons8.com/color/192/000000/futurama-bender.png" alt="Wanisah Logo">
</p>

<h3 align="center">Your Personal, Offline-First Voice Assistant for the Linux Desktop</h3>

<p align="center">
  <img alt="Python Version" src="https://img.shields.io/badge/python-3.9%2B-blue.svg">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-green.svg">
  <img alt="Platform" src="https://img.shields.io/badge/platform-Linux-lightgrey.svg">
</p>

---

**Wanisah** is a simple, hackable, and privacy-focused voice assistant designed to run completely on your local machine. Control your desktop, open apps, and get answers to your questions — all without your data ever leaving your computer.

---

## 🎥 Demo

_It's highly recommended to record a short GIF of the assistant in action and place it here._

---

## ✨ Features

- 🧠 **Offline AI Chat**: Uses a local GPT4All model to understand and respond to conversational queries. No internet required for the AI brain.
- 🗣️ **Natural Voice Interaction**: High-quality text-to-speech provided by Google for a more natural-sounding voice.
- 🖥️ **Desktop Control**: Natively integrates with the Qtile window manager to perform actions like switching workspaces.
- 🚀 **Application Launcher**: Open any application on your system, like Rofi or your terminal, with a simple voice command.
- 🌐 **Web Launcher**: Quickly open frequently used websites like YouTube or Google.
- ✅ **Zero Configuration**: An easy-to-use installation script handles all dependencies for you.
- 🔧 **Easily Extendable**: Add your own custom commands with just a few lines of Python.

---

## ⚙️ Requirements

- **Operating System**: Arch Linux (or a derivative like Manjaro)
- **Hardware**: A working microphone
- **Internet**: Required for the initial model download and for the high-quality voice, but the core AI is offline

---

## 🚀 Getting Started

### 1. Installation

Getting Wanisah set up is handled by a simple installation script.

```bash
chmod +x install.sh
./install.sh
```
````

> The script installs all system and Python dependencies. You will be prompted for your password for system-level installs.

---

### 2. First Run

Navigate to the project directory and start the assistant:

```bash
python main.py
```

**Note**: The first run downloads the AI model (~2 GB). This is a one-time download and may take a few minutes.

Once ready, the assistant will announce:

> "System online. I am ready to assist you."

---

## 🎤 Usage

Simply speak to the assistant naturally. It is always listening.

| Command                          | Action                                     |
| -------------------------------- | ------------------------------------------ |
| `Open Rofi`                      | Launches the Rofi application launcher.    |
| `Go to workspace 2`              | Switches to the second workspace in Qtile. |
| `Open YouTube`                   | Opens youtube.com in your browser.         |
| `What is the capital of France?` | Gets a conversational answer from the AI.  |
| `Tell me a joke`                 | The AI will tell you a joke.               |
| `Jarvis quit`                    | Closes the assistant.                      |

---

## 🛠️ Customization: Adding Your Own Commands

You can easily teach Wanisah new tricks by editing the `main.py` file.

1. Open `main.py` in a text editor.
2. Find the `while True:` loop at the bottom of the file.
3. Add a new `elif` block with your desired command and action.

**Example: Add a command to open your file manager (Thunar)**

```python
elif 'open my files' in query:
    speak("Opening your file manager.")
    subprocess.run(["thunar"])
```

---

## ⚠️ Troubleshooting

**"Sorry, I could not recognize your voice."**

This usually means your microphone isn't set up correctly. You can use the PulseAudio Volume Control tool to fix it.

Install it with:

```bash
sudo pacman -S pavucontrol
```

Run it by typing `pavucontrol` in your terminal.

Go to the **Input Devices** tab and make sure the correct microphone is selected as the default (click the ✔️ button).

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

```

```
