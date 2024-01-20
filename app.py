from dotenv import dotenv_values
from pathlib import Path
import openai
from src.utils.toSpeech import speak
from src.utils.toText import record_audio

config = dotenv_values('.env')
openai.api_key = config["GPT_KEY"]

speech_file_path = record_audio(6)

translation = openai.audio.translations.create(
     model="whisper-1",
    file=Path(speech_file_path),
)


gpt_response = openai.chat.completions.create( #input transcribed text as GPT prompt
    model="gpt-3.5-turbo",
    messages=[{
        "role": "system",
        "content": translation.text
    }]
)

speak(gpt_response.choices[0].message.content) #get the string data from the translation object

