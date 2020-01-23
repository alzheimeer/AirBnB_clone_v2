#!/usr/bin/python3
""" flask """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    '''close storage'''
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def h1():
    '''config html route and featch data'''
    s = list(storage.all('State').values())
    s.sort(key=lambda state: state.name)
    c = list(storage.all('City').values())
    c.sort(key=lambda cities: cities.name)
    a = list(storage.all('Amenity').values())
    a.sort(key=lambda amenities: amenities.name)
    p = list(storage.all('Place').values())
    p.sort(key=lambda places: places.name)

    return render_template('100-hbnb.html', s=s, c=c, a=a, p=p)


if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)
