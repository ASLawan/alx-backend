#!/usr/bin/env python3
"""
    Module implementing a basic flask application

"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """Renders index page"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
