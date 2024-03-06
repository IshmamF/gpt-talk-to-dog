from flask import Flask, request, jsonify
from app import gptAnswer, checkPrompt
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def landing():
    return 'Hello, World!'

@app.route("/gptanswer", methods=['POST'])
def getAnswer():
    request_data = request.get_json()
    prompt = request_data['question']
    if len(prompt) == 0:
        answer = 'The request was empty.'
    elif checkPrompt(prompt):
        answer = 'The request is under suspicion of being a prompt injection or jailbreak attack'
    else:
        answer = gptAnswer(request_data['question'])
    return jsonify({"answer": answer})

app.run()
