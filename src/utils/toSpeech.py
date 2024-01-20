from pathlib import Path
from openai import OpenAI
from dotenv import dotenv_values
config = dotenv_values('.env')
gpt_key = config['GPT_KEY']

client = OpenAI(api_key=gpt_key)

speech_file_path = Path(__file__).parent / 'public' / 'audio.mp3'

response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="I have been born again"
)

response.stream_to_file('audio.mp3')




