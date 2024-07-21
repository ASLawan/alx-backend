#!/usr/bin/env python3
"""
    Module implmenting a basic flask app with
    i18n support

"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config:
    """Class defining i18n default values"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determines the best match from supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """default app route"""
    home_title = gettext("home_title")
    home_header = gettext("home_header")
    return render_template('3-index.html',
                           home_title=home_title, home_header=home_header)


def _():
    """Handles translations"""
    pass


if __name__ == "__main__":
    app.run(debug=True)
