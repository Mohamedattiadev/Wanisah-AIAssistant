import gtts
import subprocess
# The playsound and win32com libraries are no longer needed.

def gttsSpeak(query):
    """
    This function takes text, saves it as an MP3 using Google's Text-to-Speech,
    and then plays it using the mpg123 command-line player.
    """
    try:
        tts = gtts.gTTS(text=query, lang="en", slow=False)
        tts.save("response.mp3")
        # Use subprocess to call the reliable mpg123 player
        subprocess.run(["mpg123", "response.mp3"])
    except Exception as e:
        print(f"An error occurred in gttsSpeak: {e}")


def winSpeak(query):
    """
    This is the original Windows-specific function. It will not be used
    on Linux and is left here for reference.
    """
    print("Note: winSpeak is a Windows-only function and is not being used.")
    pass


# from vosk import Model,KaldiRecognizer
# import pyaudio
#
# model = Model("./vosk/vosk-model-small-en-in-0.4")
# recognizer = KaldiRecognizer(model, 16000)
#
# mic = pyaudio.PyAudio()
# stream = mic.open(rate=1600, channels=1, format=pyaudio.paInt16, input=True,
#                   frames_per_buffer=8192)
# stream.start_stream()
# while True:
#       data = stream.read(4096)
#       if recognizer.AcceptWaveform(data):
#           print(recognizer.Result())
