from dotenv import dotenv_values
from pathlib import Path
import openai
from utils.toSpeech import speak
from utils.toText import record_audio

config = dotenv_values('.env')
openai.api_key = config["GPT_KEY"]

speech_file_path = record_audio(6)

models = {
    "text-only": "gpt-3.5-turbo",
    "txt-img": "gpt-4-vision-preview"
}
context = "we are inside the museum of natural history in NYC and you are currently helping a legally blind female user"
#context could be fed in through multiple ways 

transcription = openai.audio.transcriptions.create(
    model="whisper-1",
    file=Path(speech_file_path),
)

print(f"Your prompt is: {transcription.text}") # print the prompt that was registered

gpt_response = openai.chat.completions.create( #input transcribed text as GPT prompt
    model=models["text-only"],
    messages=[
        {"role": "system", "content": "you are a concise and helpful robotic quadruped dog named spot made by boston dynamics, that is a tour guide with a texan accent"}, # give a personality to the model
        {"role": "assistant", "content": context}, # add extra context to the user's req
        {"role": "user", "content": transcription.text} # user's req/prompt
    ],
    max_tokens = 250
)

speak(gpt_response.choices[0].message.content) #get the string data from the translation object

