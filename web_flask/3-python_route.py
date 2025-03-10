#!/usr/bin/python3
''' start a flask web app '''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    ''' returns "Hello HBNB!" for the route "/" '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    ''' returns "HBNB!" for the route "/" '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    ''' returns "C {text}" '''
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    ''' returns "python {text}" '''
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
