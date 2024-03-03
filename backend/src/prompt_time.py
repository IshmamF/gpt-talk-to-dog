#checking the statistics of the prompt times
#writing them to a txt file
from pathlib import Path
import os
import time
from dotenv import dotenv_values
import openai
from app import gptAnswer
from datetime import datetime
import json

file = Path.cwd() / 'backend' / 'src' / 'test_output' / 'test.txt' 
config = dotenv_values('.env')
openai.api_key = config["GPT_KEY"]


generate_prompt = "generate fifteen questions that I can ask a generative AI smart assistant which is located in a museum to help me since I have accessibility issues. put them in a python dictionary in the format {prompt: generated question here, time: ''}"

def query_gpt(prompt=generate_prompt) -> str:
    #this can be turned into one query by returning json.
    context = "you are helping the user by generating a prompt that will be used for a generative AI assistant to assist individuals with accssibility issues"

    gpt_response = openai.chat.completions.create( #input transcribed text as GPT prompt
        model="gpt-3.5-turbo",
        response_format= {"type": "json_object"},
        messages=[
            {"role": "assistant", "content": context}, # add extra context to the user's req
            {"role": "system", "content": "You are a helpful assistant designed to output JSON containing whatever the user requires."},
            {"role": "user", "content": prompt}
        ],
    )
    return gpt_response.choices[0].message.content


def calc_time(prompt: str) -> str:
    #given a prompt we will see how long our model takes to respond
    start_time = time.time()
    gptAnswer(prompt)
    time_delta = str(time.time() - start_time)
    return time_delta


#creating prompts with out of the box gpt....
prompts_and_timing = [json.loads(query_gpt())]

#benchmarking the time with 'spot' gpt assistant....
for item in prompts_and_timing[0]:
    prompts_and_timing[0][item]['time'] = calc_time(prompts_and_timing[0][item]['prompt'])
    

#writing to the file....
num_q = len(prompts_and_timing)
if not os.path.exists(file):
    with open(file, 'w') as initiateFile:
        initiateFile.write(f"Logging Timings of various prompts to see the query time of GPT (registered at: {datetime.now().strftime('%m/%d/%Y %H:%M:%S')})\n")
        avg_time = 0.0
        for item in prompts_and_timing[0]:
            avg_time += float(prompts_and_timing[0][item]['time'])
            initiateFile.write(f"The prompt was: {prompts_and_timing[0][item]['prompt']}, time: {prompts_and_timing[0][item]['time']}s\n")
        initiateFile.write(f"Average time taken for each prompt was roughly: {round(avg_time / len(prompts_and_timing[0]), 3)}s\n")
else: #handle the updates 
    with open(file, 'a') as updateFile:
        updateFile.write(f"\nThis was a new update (registered at: {datetime.now().strftime('%m/%d/%Y %H:%M:%S')})\n")
        avg_time = 0.0
        for item in prompts_and_timing[0]:
            avg_time += float(prompts_and_timing[0][item]['time'])
            updateFile.write(f"The prompt was: {prompts_and_timing[0][item]['prompt']}, time: {prompts_and_timing[0][item]['time']}s\n")
        updateFile.write(f"Average time taken for each prompt was roughly: {round(avg_time / len(prompts_and_timing[0]), 3)}s\n")




