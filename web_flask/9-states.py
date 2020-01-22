#!/usr/bin/python3
""" flask """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    '''close storage'''
    storage.close()

@app.route('/states', strict_slashes=False)
@app.route('/states/<n>', strict_slashes=False)
def h1(n=None):
    '''config html route and featch data'''
    s = list(storage.all('State').values())
    s.sort(key=lambda state: state.name)
    c = list(storage.all('City').values())
    c.sort(key=lambda cities: cities.name)
    xid=None
    for x in s:
        if x.id == n:
            xid = x.name
    return render_template('9-states.html', list1=s, c=c, idn=n, xid=xid)


if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)
