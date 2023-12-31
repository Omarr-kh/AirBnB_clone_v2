#!/usr/bin/python3
''' start a flask web app '''
import flask

app = flask.Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


def hello


if __name__ == "__main__":
    app.run()
