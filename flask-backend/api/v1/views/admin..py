from flask import render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from api.v1.views import app_views
from agent import Agent


db = SQLAlchemy(app_views)

@app_views.route('/')
def index():
   return render_template("index.html")
  
@app_views.route('/agent_form', methods=['POST'])
def my_form():
    username = request.form['name']
    email = request.form['email']
    password = request.form['password']
    # Now that get value back to server can send it to a DB(use Flask-SQLAlchemy)
    ag = Agent(username, email, password)
    db.create_all() # In case user table doesn't exists already. Else remove it.    
    db.session.add(ag)
    db.session.commit()

# db.session.commit()
    return (jsonify(Agent.query.all()))


 
if __name__ == '__main__':
   app_views.run(debug=True)