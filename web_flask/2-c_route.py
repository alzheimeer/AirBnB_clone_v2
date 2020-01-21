#!/usr/bin/python3
""" flask """
from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''print'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def h():
    '''print2'''
    return 'HBNB'


@app.route('/c/<name>')
def h2(name):
    '''print2'''
    return 'C {}'.format(name)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
