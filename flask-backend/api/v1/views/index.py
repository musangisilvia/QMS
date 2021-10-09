#!/usr/bin/python
"""
    The landing page
"""
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
        Returns status of app
    """
    return (jsonify({'status': 'ok'}))