#!/bin/bash

echo "--- Installing System Dependencies (Requires Password) ---"
sudo pacman -S --needed --noconfirm python python-pip portaudio espeak ffmpeg mpg123

echo "\n--- Installing Python Libraries ---"
pip install SpeechRecognition PyAudio pyttsx3 gpt4all gtts

echo "\n--- Installation Complete! ---"
echo "You can now run Wanisah by running the 'python main.py' command."
echo "The first time you run it, it will download the AI model (about 2GB). Please be patient."
