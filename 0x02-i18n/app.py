#!/usr/bin/env python3
"""
Flask app to display the current time based on the inferred time zone
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
import pytz
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    """Get user details from user table by ID"""
    return users.get(user_id)

@app.before_request
def before_request():
    """Set user as global g variable based on login_as parameter"""
    user_id = int(request.args.get('login_as', 0))
    g.user = get_user(user_id) if user_id else None

@babel.localeselector
def get_locale():
    """Determine the best match for locale based on request or user's preference"""
    locale = request.args.get('locale') if request.args.get('locale') in app.config['LANGUAGES'] else None
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'], default=app.config['BABEL_DEFAULT_LOCALE'])

@babel.timezoneselector
def get_timezone():
    """Determine the best match for timezone based on request or user's preference"""
    timezone = request.args.get('timezone')
    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']

@app.route('/')
def index():
    """Render the index.html template with current time based on the inferred time zone"""
    current_time = datetime.now(pytz.timezone(get_timezone())).strftime("%b %d, %Y, %I:%M:%S %p")
    message = gettext('current_time_is', current_time=current_time)
    return render_template('index.html', username=g.user["name"] if g.user else None, current_time_message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

