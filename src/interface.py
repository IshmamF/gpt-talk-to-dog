from flask import Flask, render_template, url_for

app = Flask(__name__)

url_for('static', filename='styles.css')

@app.route("/")
def landing():
    return render_template('index.html', navigation=[
        {"href":"/textPrompt", "title":"textPrompt"},
        {"href":"/speechPrompt", "title":"speechPrompt"},
        {"href":"/imagePrompt", "title":"imagePrompt"},
        {"href":"/speak", "title":"speak"}
    ])

@app.route("/textPrompt") #in the case we need to add data to a DB, we should add the responses generated and the audio clippings
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
    return render_template('speakOutput.html', output="This will be implemented")
