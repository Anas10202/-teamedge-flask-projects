from flask import Flask, render_template , json ,jsonify, current_app as app
from datetime import date
import requests
import os

@app.route('/')
def index():
    return  "Welcome to Anas's holiday Project"
@app.route('/holiday')
def show_holiday():
    year=str(date.year())
    response=request.get


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')