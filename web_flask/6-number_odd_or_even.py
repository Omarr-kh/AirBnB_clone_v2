#!/usr/bin/python3
''' start a flask web app '''
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def n_route(n):
    ''' "n is a number" '''
    return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    ''' display a HTML page only if n is an integer '''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    ''' display a HTML page only if n is an integer '''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
