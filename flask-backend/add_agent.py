from enum import unique
import re
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Ghostjoys17@localhost/qmsData'
db = SQLAlchemy(app)

class Agent(db.Model):
    """
        Class to define the Agent table
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    counter = db.Column(db.Integer)

    def __init__(self, username, email, password, counter):
        self.name = username
        self.email = email
        self.password = password
        self.counter = counter


    def __repr__(self):
        return "<Name: {}>".format(self.name)

@app.route("/add_agent", methods=['GET', 'POST'])
def add_agent():
    if request.form:
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        counter = request.form.get("counter")
        agent = Agent(name, email, password, counter)
        db.create_all()
        db.session.add(agent)
        db.session.commit()
    
    return (render_template("add_agent.html"))
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)