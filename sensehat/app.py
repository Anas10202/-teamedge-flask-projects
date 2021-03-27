from flask import Flask, render_template , redirect, request,url_for,json ,jsonify, current_app as app
from datetime import date
from sense_hat import SenseHat
import requests
import os

app = Flask(__name__)
sense = SenseHat()

@app.route('/received/<name>')
def success(name):
    return name,sense.show_message(name)

@app.route('/message', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user= request.form['nm']
        return redirect(url_for('success', name = user))
    else:
        user = request.args.get('nm')
        return render_template('login.html', name = user)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')