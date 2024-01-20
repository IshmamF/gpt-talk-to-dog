from dotenv import dotenv_values
import wave
import sys
import pyaudio
from pathlib import Path
import openai
from src.utils.toSpeech import speak

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100

config = dotenv_values('.env')
openai.api_key = config["GPT_KEY"]

def record_audio(seconds: int):
    output_path = "output.wav"
    with wave.open(output_path, "wb") as wf:
        p = pyaudio.PyAudio()
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)
        print("Recording...")
        for index in range(0, RATE // CHUNK * seconds):
            if index % (RATE // CHUNK) == 0:
                print(f"{index // (RATE // CHUNK)} / {seconds}s")
            wf.writeframes(stream.read(CHUNK))
        print("DONE")

        stream.close()
        p.terminate()
    print(f"File saveed at {output_path}")
    return output_path

speech_file_path = record_audio(5)

audio_file = open(speech_file_path, 'rb')

translation = openai.audio.translations.create(
        model="whisper-1",
        file=Path(speech_file_path),
    )

speak(translation.__getattribute__('text')) #get the string data from the translation object