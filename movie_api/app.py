from flask import Flask, render_template , json ,jsonify, current_app as app
from datetime import date
import requests
import os

app = Flask(__name__)
movies_data = os.path.join(app.static_folder, 'data','movies.json')

@app.route('/api/v1/movies/all', methods=['GET'])
def show_movies():
    with open(movies_data,'r') as jsondata:
         movies = json.load(jsondata)
    return render_template('movies.html',movies=movies)
    


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
