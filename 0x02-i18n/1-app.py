#!/usr/bin/env python3

""" Basic Flask app.
"""

from flask import Flask, render_template
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
        Languages (list): List of supported languages.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Apply the configuration to the Flask app
app.config.from_object(Config)


# Define the route for the root URL
@app.route('/')
def index():
    """Render the index page."""
    return render_template('1-index.html')


# Main entry point of the application
if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
