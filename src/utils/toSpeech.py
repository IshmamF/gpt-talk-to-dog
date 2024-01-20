from pathlib import Path
from openai import OpenAI
from dotenv import dotenv_values
import pygame
import time
config = dotenv_values('.env')
gpt_key = config['GPT_KEY']

def speak(txt_input, model='tts-1-hd', voice='onyx'):
    client = OpenAI(api_key=gpt_key)

    speech_file_path = Path(__file__).parent / 'public' / 'audio.mp3'

    start_time = time.time()

    # Initialize Pygame Mixer
    pygame.mixer.init()

    response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=txt_input
    )

    response.stream_to_file('audio.mp3') # FIXME: use the non deprecated version 

    pygame.mixer.music.load('audio.mp3')
    print(f"Time to play: {time.time() - start_time} seconds")
    pygame.mixer.music.play()

    # Loop to keep the script running during playback
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)



