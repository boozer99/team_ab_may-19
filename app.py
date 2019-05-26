from flask import Flask, render_template, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import MySQLdb


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///sql12293343.db '
app.config['DEBUG'] = True
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

@app.route("/",methods=['POST'])
def main():
    db.session.add(name)
    db.session.commit()

    

if __name__ == "_main_":
   app.run(debug=True)
