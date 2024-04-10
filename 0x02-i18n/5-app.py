#!/usr/bin/env python3
"""
Flask app to demonstrate mock logging in and displaying messages based on login status
"""

from flask import Flask, render_template, g
import pytz

app = Flask(__name__)

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

@app.route('/')
def index():
    """Render the index.html template with appropriate message based on login status"""
    message = render_template('5-index.html', username=g.user["name"] if g.user else None)
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

