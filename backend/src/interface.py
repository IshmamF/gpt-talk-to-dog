from flask import Flask, request, jsonify
from app import gptAnswer, checkPrompt
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def landing():
    return 'This is the web service for the spot interface'

@app.route("/gptanswer", methods=['POST'])
def getAnswer():
    request_data = request.get_json()
    prompt = request_data['question']
    if len(prompt) == 0:
        answer = 'The request was empty.'
    elif checkPrompt(prompt):
        answer = 'The request is under suspicion of being a prompt injection or jailbreak attack'
    else:
        answer = gptAnswer(prompt, request_data['context'])
    return jsonify({"answer": answer})

app.run()
