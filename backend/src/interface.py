from flask import Flask, render_template, url_for, request, jsonify
from app import gptAnswer
from flask_cors import CORS
from flask import send_file
from pathlib import Path
from utils.toSpeech import speak

app = Flask(__name__)
CORS(app)

#url_for('static', filename='styles.css')

@app.route('/')
def landing():
    return 'Hello, World!'

@app.route("/gptanswer", methods=['POST'])
def getAnswer():
    request_data = request.get_json()
    answer = gptAnswer(request_data['question'])
    return jsonify({"answer": answer})

@app.route("/gptspeakanswer", methods=['GET', 'POST'])#deals with speech input
def getSpokenAnswer():
    if request.method == 'GET':
        return send_file(Path.cwd()/'backend'/'src'/'audio'/'audio.mp3', mimetype='audio/mp3')
    request_data = request.get_json()
    answer = gptAnswer(request_data['question'])
    speak(answer)
    return 'successfully created file'



app.run()
