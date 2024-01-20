from dotenv import dotenv_values
from pathlib import Path
import openai
from src.utils.toSpeech import speak
from src.utils.toText import record_audio

config = dotenv_values('.env')
openai.api_key = config["GPT_KEY"]

speech_file_path = record_audio(5)

translation = openai.audio.translations.create(
        model="whisper-1",
        file=Path(speech_file_path),
    )

speak(translation.text) #get the string data from the translation object