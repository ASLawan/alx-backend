#!/usr/bin/env python3
"""
    Module implmenting a basic flask app with
    i18n support

"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Class defining i18n default values"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """default app route"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
