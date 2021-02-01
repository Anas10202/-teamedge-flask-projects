from flask import Flask, render_template , json ,jsonify, current_app as app
from datetime import date
import requests
import os

app = Flask(__name__)



@app.route('/')
def index():
    name='Anas'
    colors=['purple','blue','green','yellow']
    return render_template('index.html',greeting=name,colors=colors)
@app.route('/about')
def about():
    return '<h1>About</h1><p>some other content</p>'
@app.route('/nasa')
def show_nasa_pic():
    today=str(date.today())
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date='+today)
    data=response.json()
    return render_template('nasa.html',data=data)

albums_data = os.path.join(app.static_folder, 'data','albums.json')

@app.route('/api/v1/albums/all', methods=['GET'])
def show_album():
    with open(albums_data,'r') as jsondata:
         albums = json.load(jsondata)
    return jsonify(albums)

movies_data = os.path.join(app.static_folder, 'data','movies.json')

@app.route('/api/v1/movies/all', methods=['GET'])
def show_movies():
    with open(movies_data,'r') as jsondata:
         movies = json.load(jsondata)
    return render_template('movies.html',movies=movies)
    


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
