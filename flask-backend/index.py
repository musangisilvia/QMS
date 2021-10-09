from re import S
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Ghostjoys17@localhost/qmsData'
db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.form:
        print(request.form)
    return (render_template("index.html"))
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)