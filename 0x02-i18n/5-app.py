#!/usr/bin/env python3
"""
    Module implmenting a basic flask app with
    i18n support and mock user login

"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Class defining i18n default values"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determines the best match from supported languages"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Returns user by user id from login mock dictionary"""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
        # try:
        #    user_id = int(user_id)
        #    return users.get(user_id)
        # except ValueError:
        #   return None
    return None


@app.before_request
def before_request():
    """Executes before all other functions"""
    g.user = get_user()


@app.route('/')
def index():
    """default app route"""
    home_title = _("home_title")
    home_header = _("home_header")
    return render_template('5-index.html',
                           home_title=home_title,
                           home_header=home_header)


if __name__ == "__main__":
    app.run(debug=True)
