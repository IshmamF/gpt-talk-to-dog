from flask import Flask, render_template, url_for, request, jsonify
from app import gptAnswer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#url_for('static', filename='styles.css')

"""@app.route("/")
def landing():
    return render_template('index.html', navigation=[
        {"href":"/textPrompt", "title":"textPrompt"},
        {"href":"/speechPrompt", "title":"speechPrompt"},
        {"href":"/imagePrompt", "title":"imagePrompt"},
        {"href":"/speak", "title":"speak"}
    ])"""

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/gptanswer", methods=['POST'])
def getAnswer():
    request_data = request.get_json()
    answer = gptAnswer(request_data['question'])
    return jsonify({"answer": answer})

app.run()
"""@app.route("/textPrompt") #in the case we need to add data to a DB, we should add the responses generated and the audio clippings
def textPrompt():
    return render_template('text.html', methods=['GET', 'POST'])
        
@app.route("/speechPrompt", methods=['GET', 'POST'])
def speechPrompt():
    return render_template('speech.html')

@app.route("/imagePrompt", methods=['GET', 'POST'])
def imagePrompt():
    return render_template('image.html')

@app.route("/speak", methods=['GET', 'POST'])
def output():
    return render_template('speakOutput.html', output="This will be implemented")"""
