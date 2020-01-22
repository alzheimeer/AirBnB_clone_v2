#!/usr/bin/python3
""" flask """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    '''close storage'''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def h1():
    '''config html route and featch data'''
    s = list(storage.all('State').values())
    s.sort(key=lambda state: state.name)
    return render_template('7-states_list.html', list1=s)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
