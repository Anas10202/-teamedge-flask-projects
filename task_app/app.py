from flask import Flask, render_template , redirect, request,url_for,json ,jsonify, current_app as app
from datetime import date
from sense_hat import SenseHat
import requests
import os
import sqlite3
from flask_apscheduler import APScheduler

app = Flask(__name__)
sense = SenseHat()

@app.route('/',methods=['POST','GET'])
def remind():
    if request.method == 'POST':
        message= request.form['nm']
        time=request.form['remindertime']
        sense.show_message(message)

        return render_template('reminder.html', message = message, time=time)
    else:
        message = request.args.get('nm')
        time=request.args.get('remindertime')
    
        return render_template('reminder.html', message = message, time=time)




if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')