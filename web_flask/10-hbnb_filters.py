#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models import storage
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters(state_id=None):
    """ display a HTML page like 6-index.html """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_session(exception):
    """ teardown storage """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
