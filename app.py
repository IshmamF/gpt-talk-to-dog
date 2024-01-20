from dotenv import dotenv_values
import wave
import sys
import pyaudio
from pathlib import Path
import openai

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


import time
import pygame

def not_streamed(input_text, model='tts-1', voice='alloy'):
    start_time = time.time()

    # Initialize Pygame Mixer
    pygame.mixer.init()

    response = openai.audio.speech.create(
        model=model, 
        voice=voice,
        input=input_text,
    )

    response.stream_to_file("output.opus")

    # Load and play the audio file
    pygame.mixer.music.load('output.opus')
    print(f"Time to play: {time.time() - start_time} seconds")
    pygame.mixer.music.play()

    # Loop to keep the script running during playback
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

not_streamed(translation.text)