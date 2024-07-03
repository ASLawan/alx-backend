#!/usr/bin/env python3
"""
    Module implmenting a basic flask app with
    i18n support, url parameter

"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


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
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """default app route"""
    home_title = _("home_title")
    home_header = _("home_header")
    return render_template('4-index.html',
                           home_title=home_title, home_header=home_header)


if __name__ == "__main__":
    app.run(debug=True)
