#!/usr/bin/python3
""" Starts Flask web app """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbn():
    """ Returns Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns HBNB """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
