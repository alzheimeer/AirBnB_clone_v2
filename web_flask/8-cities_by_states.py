#!/usr/bin/python3
""" flask """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    '''close storage'''
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def h1():
    '''config html route and featch data'''
    s = list(storage.all('State').values())
    s.sort(key=lambda state: state.name)
    c = list(storage.all('City').values())
    c.sort(key=lambda cities: cities.name)

    return render_template('8-cities_by_states.html', list1=s, c=c)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
