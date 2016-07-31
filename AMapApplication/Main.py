from flask import Flask
from flask import render_template
from os import environ
import Function
import requests
app = Flask(__name__)

# key=43a462f629d817bf91ca4bb95f9cd7b3
@app.route('/')
def hello_world():
    return render_template(
        'Search.html'
    )
#192.168.191.1:8080
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 5000
    app.debug = True
    app.run(HOST, PORT)
