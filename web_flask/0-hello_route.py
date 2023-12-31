#!/usr/bin/python3
''' start a flask web app '''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    ''' returns "Hello HBNB!" for the route "/" '''
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
