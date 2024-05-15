#!/usr/bin/env python3

""" Basic Flask app with mocked user login system.
Instantiate the Babel object and configure the app to support multiple languages.
Create a Config class with the following attributes:
    LANGUAGES(list): List of supported languages.
    BABEL_DEFAULT_LOCALE(str): Default language for the app.
    BABEL_DEFAULT_TIMEZONE(str): Default timezone for the app.
Define the route for the root URL.
Create a get_locale function with the babel.localeselector decorator.
Use request.accept_languages to determine the best match with our supported languages.
Implement a mocked user login system.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

# Initialize the Flask application
app = Flask(__name__)
# Instantiate the Babel object
babel = Babel(app)


# Create the Config class
class Config:
    """
    Configuration class for the application.
    Attributes:
        LANGUAGES (list): List of supported languages.
        BABEL_DEFAULT_LOCALE (str): Default language for the app.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Apply the configuration to the Flask app
app.config.from_object(Config)

# User table to mock a database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    # Check if the locale parameter is present in the request
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Check if the user is logged in and has a locale preference
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Get user from the request.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Execute before each request to retrieve user information.
    Retreives the user and assigns it to the global variable g.user.
    """
    g.user = get_user()


# Define the route for the root URL
@app.route('/', strict_slashes=False)
def index() -> str:
    """Render the index page."""
    return render_template('5-index.html')


# Main entry point of the application
if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(port="5000", host="0.0.0.0", debug=True)