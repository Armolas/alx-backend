#!/usr/bin/env python3
'''babel flask'''
from flask import Flask, render_template, request
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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''The home page'''
    return render_template('2-index.html')
