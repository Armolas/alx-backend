#!/usr/bin/env python3
'''babel flask'''
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)


class Config:
    '''The configuration class'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''gets the language'''
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    lang = g.user['locale']
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    '''gets a user details'''
    user_id = request.args.get('login_as')
    user_id = int(user_id)
    if user_id in users:
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    '''sets a global user'''
    user = get_user()
    g.user = user


@app.route('/')
def index():
    '''The home page'''
    return render_template('6-index.html')
