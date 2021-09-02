from flask import Flask, render_template
import doer
import json

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')