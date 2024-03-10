from flask import Flask, render_template, url_for, request, jsonify
from app import gptAnswer
from flask_cors import CORS
from flask import send_file
from pathlib import Path

app = Flask(__name__)
CORS(app)

@app.route('/')
def landing():
    return 'This is the web service for the spot interface'

@app.route("/gptanswer", methods=['POST'])
def getAnswer():
    request_data = request.get_json()
    answer = 'The request was empty.' if len(request_data['question']) == 0 else gptAnswer(request_data['question'], request_data['context'])
    return jsonify({"answer": answer})

app.run()
