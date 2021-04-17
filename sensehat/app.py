from flask import Flask, render_template , redirect, request,url_for,json ,jsonify, current_app as app
from datetime import date
from sense_hat import SenseHat
import requests
import os
import sqlite3

app = Flask(__name__)
sense = SenseHat()

@app.route('/received/<message>')
def success(message):
    return message

@app.route('/message', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        message= request.form['nm']
        sense.show_message(message)
        

        conn = sqlite3.connect('./static/data/messages.db')
        curs = conn.cursor()
        curs.execute("INSERT INTO messages (message) VALUES(?)",(message,))
        conn.commit()
        conn.close()

       
        return redirect(url_for('success', message = message))
    else:
        message = request.args.get('nm')
        return render_template('login.html', message = message)

@app.route('/all')
def all():
    #connect to DB
    conn = sqlite3.connect('./static/data/messages.db')
    curs = conn.cursor()
    messages = []
    rows = curs.execute("SELECT * from messages")
    for row in rows:
        message = {'message':row[0]}
        messages.append(message)
    conn.close()
    return render_template('all.html', messages = messages)


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')