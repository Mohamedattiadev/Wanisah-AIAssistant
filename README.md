# Wanisah AI Assistant

<div align="center">
<pre>
██╗    ██╗ █████╗ ███╗   ██╗██╗███████╗ █████╗ ██╗  ██╗
██║    ██║██╔══██╗████╗  ██║██║██╔════╝██╔══██╗██║  ██║
██║ █╗ ██║███████║██╔██╗ ██║██║███████╗███████║███████║
██║███╗██║██╔══██║██║╚██╗██║██║╚════██║██╔══██║██╔══██║
╚███╔███╔╝██║  ██║██║ ╚████║██║███████║██║  ██║██║  ██║
╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
</pre>

<h3 align="center">A Smart AI Voice Assistant for the Linux Desktop</h3>

<p align="center">
<img alt="Python Version" src="https://img.shields.io/badge/python-3.11-blue.svg">
<img alt="License" src="https://img.shields.io/badge/license-MIT-green.svg">
<img alt="Platform" src="https://img.shields.io/badge/platform-Arch%20Linux-lightgrey.svg">
</p>
</div>

---

**Wanisah** is your own offline and privacy-friendly AI voice assistant, built specifically for Linux. It listens to you, talks back naturally, and helps you get things done — like opening apps, checking the weather, or managing tasks — all **without sending your voice or data to the cloud**.

---

## ✨ Key Features (Plain English)

- 🧠 **Smart Brain with Backup**: Uses Google Gemini for intelligent replies when online, and falls back to a local GPT model when offline.
- 🎤 **Private Listening**: Uses Vosk, a fully offline speech recognizer. Your voice never leaves your computer.
- 🗣️ **Clear Voice Replies**: Uses Google TTS for a natural voice. If offline, it still talks using a fast built-in voice engine.
- 🖥️ **Controls Your Desktop**: Switch workspaces, open terminals, or launch apps like Rofi — just by speaking.
- 📋 **Useful Built-in Tools**:
  - Send Emails
  - Track To-Dos
  - Get Weather Info
  - Check System Usage
  - Do Math
- 🛠️ **Customizable**: Add your own commands easily — no advanced coding required.

---

## 🚀 Getting Started (Step-by-Step)

This guide will help even non-coders set up Wanisah from scratch.

---

### 📦 Step 1: System Requirements

- ✅ You’re using **Arch Linux** or **Manjaro**
- ✅ You have a **microphone**
- ✅ You have an **internet connection** (just for setup)

---

### 🔧 Step 2: Install Python with pyenv

We'll use `pyenv` to make sure you're using the correct Python version.

#### 🧰 Install `pyenv`:

```bash
yay -S pyenv
```

#### 🧰 Configure your shell (pick one):

<details>
<summary>🐟 If you use Fish shell</summary>

Edit `~/.config/fish/config.fish` and add:

```bash
set -gx PYENV_ROOT $HOME/.pyenv
set -gx PATH $PYENV_ROOT/bin $PATH
status --is-interactive; and source (pyenv init -|psub)
```

</details>

<details>
<summary>🧪 If you use Bash or Zsh</summary>

Add this to `~/.bashrc` or `~/.zshrc`:

```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

</details>

Restart your terminal.

---

### 🐍 Step 3: Set Up Python Environment

```bash
# Install the required Python version
pyenv install 3.11.9

# Use it inside this project
pyenv local 3.11.9

# Create a virtual environment
python3.11 -m venv venv

# Activate it (pick one):
source venv/bin/activate       # For Bash/Zsh
source venv/bin/activate.fish  # For Fish shell
```

---

### 📂 Step 4: Install Wanisah

```bash
# Clone the project
git clone https://github.com/your-username/wanisah-Assistant.git
cd wanisah-Assistant

# Make install script executable
chmod +x install.sh

# Run it (you’ll be asked for your password)
./install.sh
```

---

### 🔐 Step 5: Add Your API Keys

Create a file named `keys.py` inside the `config/` folder:

```bash
touch config/keys.py
```

Paste this into the file and add your real credentials:

```python
# config/keys.py
gemini_api_key = "YOUR_GEMINI_API_KEY"
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_app_password"
```

---

### ▶️ Step 6: Run the Assistant

```bash
python main.py
```

The first time, it will download models (~2GB). This only happens once.

Once ready, it will say:

> "System online. I am ready to assist you."

---

## 🎤 What Can I Say?

| You Say...                        | Wanisah Will...                              |
| --------------------------------- | -------------------------------------------- |
| "Open Rofi"                       | Open the Rofi app launcher                   |
| "Go to workspace three"           | Switch to workspace 3 in your window manager |
| "What's the weather in Cairo?"    | Tell you the current weather                 |
| "Add ‘buy milk’ to my to-do list" | Save a reminder to your list                 |
| "What’s my CPU usage?"            | Show your system's CPU stats                 |
| "Wanisah quit"                    | Shut down the assistant                      |

---

## 🛠️ Want to Add Your Own Voice Commands?

It’s easy! You’ll just edit one file: `tools/local_commands.py`

### Example: Open Discord

```python
elif "open discord" in query:
    speak("Opening Discord.")
    subprocess.run(["discord"])
    return True
```

That's it. Save and restart Wanisah to try your new command.

---

## 🧯 Troubleshooting

**Microphone not detected?**

Install PulseAudio Volume Control:

```bash
sudo pacman -S pavucontrol
```

Then run `pavucontrol` and:

1. Go to the **Input Devices** tab
2. Make sure the correct microphone is selected
3. Click the ✔️ button to make it the default

---

## 🤝 Contribute

Have an idea? Found a bug? We welcome all feedback, issues, and pull requests. Help make Wanisah better!

---

## 📜 License

MIT License — free for personal or commercial use. See the `LICENSE` file.

---
