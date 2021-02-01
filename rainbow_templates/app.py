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
    name='Anas'
    color='purple'
    other_colors=["purple","green","blue","red","yellow","orange"]
    return render_template('colors.html' , color=color , name=name, other_colors=other_colors)
    


@app.route('/blue')
def show_blue():
    name='Anas'
    color='blue'
    other_colors=["purple","green","blue","red","yellow","orange"]
    return render_template('colors.html',color=color,name=name, other_colors=other_colors)


@app.route('/green')
def show_green():
    name='Anas'
    color='green'
    other_colors=["purple","green","blue","red","yellow","orange"]
    return render_template('colors.html',color=color,name=name, other_colors=other_colors)

@app.route('/red')
def show_red():
    name='Anas'
    color='red'
    other_colors=["purple","green","blue","red","yellow","orange"]
    return render_template('colors.html',color=color,name=name, other_colors=other_colors)

@app.route('/yellow')
def show_yellow():
    name='Anas'
    color='yellow'
    other_colors=["purple","green","blue","red","yellow","orange"]
    return render_template('colors.html',color=color,name=name, other_colors=other_colors)

@app.route('/orange')
def show_orange():
    name='Anas'
    color='orange'
    other_colors=["purple","green","blue","red","yellow","orange"]
    return render_template('colors.html',color=color,name=name, other_colors=other_colors)
@app.route('/rainbow')
def show_rainbow():
    name='Anas'
    
    other_colors=["purple","green","blue","red","yellow","orange"]
    return render_template('colors.html',name=name, other_colors=other_colors)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')