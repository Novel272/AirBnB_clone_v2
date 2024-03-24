#!/usr/bin/python3
""" 2. Script that start Flask web app with three view functions """

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ Return a type of text. """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """ Returns text. """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ replace with avariable. """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
