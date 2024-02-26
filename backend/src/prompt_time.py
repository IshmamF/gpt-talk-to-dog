#checking the statistics of the prompt times
#writing them to a txt file
from pathlib import Path
import os
import time
from dotenv import dotenv_values
import openai
from app import gptAnswer
from datetime import datetime


config = dotenv_values('.env')
openai.api_key = config["GPT_KEY"]

generate_prompt = "generate 1 question that I can ask a generative AI smart assistant which is located in a museum to help me since I have accessibility issues."

file = Path.cwd() / 'backend' / 'src' / 'test_output' / 'test.txt' 
prompts_and_timing = [{"prompt":"", "time":""} for i in range(5)]


def query_gpt(prompt=generate_prompt) -> str:
    #this can be turned into one query by returning json.
    context = "you are helping the user by generating 1 prompt that will be used for a generative AI assistant to assist individuals with accssibility issues"

    gpt_response = openai.chat.completions.create( #input transcribed text as GPT prompt
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": context}, # add extra context to the user's req
            {"role": "user", "content": prompt}
        ],
        max_tokens = 250 #cap the length of the response
    )
    return gpt_response.choices[0].message.content

def calc_time(prompt: str) -> str:
    #given a prompt we will see how long our model takes to respond
    start_time = time.time()
    gptAnswer(prompt)
    time_delta = str(time.time() - start_time)
    return time_delta


#creating prompts with out of the box gpt....
for prompt in prompts_and_timing: #we can make n amounts
        prompt["prompt"] = query_gpt()

#benchmarking the time with 'spot' gpt assistant....
for item in prompts_and_timing:
    item["time"] = calc_time(item["prompt"])

#writing to the file....
if not os.path.exists(file):
    with open(file, 'w') as initiateFile:
        initiateFile.write(f"Logging Timings of various prompts to see the query time of GPT (registered at: {datetime.now().strftime('%m/%d/%Y %H:%M:%S')})\n")
        avg_time = 0.0
        for item in prompts_and_timing:
            avg_time += float(item["time"])
            initiateFile.write(f"The prompt was: {item['prompt']}, time: {item['time']}s\n")
        initiateFile.write(f"Average time taken for each prompt was: {avg_time / len(prompts_and_timing)}s\n")
else: #handle the updates 
    with open(file, 'a') as updateFile:
        updateFile.write(f"\nThis was a new update (registered at: {datetime.now().strftime('%m/%d/%Y %H:%M:%S')})\n")
        avg_time = 0.0
        for item in prompts_and_timing:
            avg_time += float(item["time"])
            updateFile.write(f"The prompt was: {item['prompt']}, time: {item['time']}s\n")
        updateFile.write(f"Average time taken for each prompt was: {avg_time / len(prompts_and_timing)}s\n")




