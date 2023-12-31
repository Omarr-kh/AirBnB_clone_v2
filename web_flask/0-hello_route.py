#!/usr/bin/python3
''' start a flask web app '''
import flask

app = flask.Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    ''' returns "Hello HBNB!" for the route "/" '''
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
