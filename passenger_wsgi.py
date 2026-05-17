#!/usr/bin/env python
"""
Passenger WSGI entry point for cPanel deployment
This file is required for cPanel's Passenger application server
"""

import sys
import os

# Add project directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask app factory
from app import create_app

# Create Flask application instance
app = create_app()

# Set production environment
app.config['ENV'] = 'production'
app.config['DEBUG'] = False

# Passenger will look for this 'application' variable
application = app

if __name__ == '__main__':
    # For local testing only
    application.run(debug=False, host='127.0.0.1', port=5001)
