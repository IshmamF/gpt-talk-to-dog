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

# @app.route("/gptspeakanswer", methods=['GET', 'POST'])#deals with speech input
# def getSpokenAnswer():
#     if request.method == 'GET':
#         return send_file(Path.cwd()/'backend'/'src'/'audio'/'audio.mp3', mimetype='audio/mp3')
#     request_data = request.get_json()
#     answer = gptAnswer(request_data['question'])
#     speak(answer)
#     return 'successfully created file'



app.run()
