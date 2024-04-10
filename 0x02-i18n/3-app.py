#!/usr/bin/env python3
"""
Flask app with parametrized templates and translations
"""

from flask import Flask, render_template
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for Flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Determine the best match for locale based on request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index.html template with parametrized messages
    """
    return render_template('3-index.html', title=gettext('home_title'), header=gettext('home_header'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

