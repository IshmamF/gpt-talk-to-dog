from flask import Flask, render_template

app = Flask(__name__)

while True:
    app.route('/')
    def index():
        