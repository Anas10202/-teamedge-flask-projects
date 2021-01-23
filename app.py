from flask import Flask, render_template , json ,jsonify, current_app as app
from datetime import date
import requests
import os

app = Flask(__name__)
@app.route('/')
def index():
 
    return  "Welcome to Anas's rainbow Project"

@app.route('/purple')
def show_purple():
    return render_template('purple.html')
    


@app.route('/blue')
def show_blue():
    return render_template('blue.html')


@app.route('/green')
def show_green():
    return render_template('green.html')

@app.route('/red')
def show_red():
    return render_template('red.html')

@app.route('/yellow')
def show_yellow():
    return render_template('yellow.html')

@app.route('/orange')
def show_orange():
    return render_template('orange.html')


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')