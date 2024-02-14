from pathlib import Path
from openai import OpenAI
from dotenv import dotenv_values
import pygame
import time
config = dotenv_values('.env')
gpt_key = config['GPT_KEY']
client = OpenAI(api_key=gpt_key)
speech_file_path = Path.cwd()/'backend'/'src'/'audio'/'audio.mp3'

def speak(txt_input: str, model='tts-1-hd', voice='onyx'):
    response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=txt_input
    )

    response.stream_to_file(speech_file_path) # FIXME: use the non deprecated version 

if __name__== "__main__":
    speak("Hello my name is Onyx, it's a pleasure to work with you!")

