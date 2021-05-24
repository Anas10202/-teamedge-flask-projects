from flask import Flask, render_template , redirect, request,url_for,json ,jsonify, current_app as app
from datetime import date
from sense_hat import SenseHat
import requests
import os
import sqlite3
from flask_apscheduler import APScheduler

app = Flask(__name__)
scheduler=APScheduler()
scheduler.init_app(app)
scheduler.start()
sense = SenseHat()

@app.route('/',methods=['POST','GET'])
def remind():
    if request.method == 'POST':
        message= request.form['nm']
        time=request.form['remindertime']
        sense.show_message(message)


        conn = sqlite3.connect('./static/data/reminder.db')
        curs = conn.cursor()
        curs.execute("INSERT INTO messages (message,time) VALUES((?),(?))",(message,time))
        conn.commit()
        conn.close()
        
        return render_template('reminder.html', message = message, time=time)
    else:
        message = request.args.get('nm')
        time=request.args.get('remindertime')
    
        return render_template('reminder.html', message = message, time=time)
@app.route('/all')
def all():
    #connect to DB
    conn = sqlite3.connect('./static/data/reminder.db')
    curs = conn.cursor()
    messages = []
    rows = curs.execute("SELECT * from messages")
    for row in rows:
        message = {'message':row[0],'time':row[1],'rowid':row[2]}
        messages.append(message)
    conn.close()

   scheduler.add_job(id=row[2], func='show_remind', trigger='time', run_date=row[1], args=row[0])
    return render_template('all.html', messages = messages)


@app.route('/button/delete/<btn>')
def delete(btn):
    #connect to DB
    conn = sqlite3.connect('./static/data/reminder.db')
    curs = conn.cursor()
    curs.execute("DELETE from messages WHERE rowid=(?)",(btn,))
    conn.commit()
    conn.close()
    return redirect(url_for('all'))

@app.route('/button/edit/<btn>')
def edit(btn):
    #connect to DB
    conn = sqlite3.connect('./static/data/reminder.db')
    curs = conn.cursor()
    curs.execute("UPDATE messages(message,time) VALUES((?),(?)) WHERE rowid=(?)",(btn,))
    conn.commit()
    conn.close()
    return render_template('all.html')
def show_reminder(reminder):
    sense.show_message(args)
    return 0


    




if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')