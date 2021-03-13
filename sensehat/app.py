from flask import Flask, render_template , redirect, request,url_for,json ,jsonify, current_app as app
from datetime import date
import requests
import os

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user= request.form['nm']
        return redirect(url_for('success', name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name = user))


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')