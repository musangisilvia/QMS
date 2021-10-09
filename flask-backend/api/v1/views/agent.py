#!/usr/bin/python
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from api.v1.views import app_views

"""
    This module contains the agent class for the ORM
"""

app_views.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Ghostjoys17@localhost/qmsData'
db = SQLAlchemy(app_views)

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    pwd = db.Column(db.String(120))

    def __init__(self, username, email, pwd):
        self.username = username
        self.email = email
        self.pwd = pwd

    def __repr__(self):
        return '<User %r>' % self.username


@app_views.route('/agents')
def all_agent():
    """
        returns all agents in the db
    """
    return (jsonify(Agent.query.all()))

# admin = User('silvia', 'silvia@example.com')

# db.create_all() # In case user table doesn't exists already. Else remove it.    

# db.session.add(admin)

# db.session.commit() # This is needed to write the changes to database

# User.query.all()

# User.query.filter_by(username='admin').first()