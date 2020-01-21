#!/usr/bin/python3
""" flask """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def h0():
    '''print'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def h1():
    '''print2'''
    return 'HBNB'


@app.route('/c/<name>')
def h2(name):
    '''print2'''
    return 'C {}'.format(name.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<name>')
def h3(name='is cool'):
    '''print3'''
    return 'Python {}'.format(name.replace('_', ' '))


@app.route('/number/<int:n>')
def h4(n):
    '''print4'''
    if isinstance(n, int):
        return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def h5(n):
    '''print5'''
    if isinstance(n, int):
        return render_template('5-number.html', n5=n)


@app.route('/number_odd_or_even/<int:n>')
def h6(n):
    '''print6'''
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', n6=n)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
