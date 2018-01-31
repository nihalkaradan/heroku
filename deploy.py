from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_restless import APIManager


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'

db = SQLAlchemy(app)

class  users(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(200),unique=True,nullable=False)
db.create_all()	



manager=APIManager(app,flask_sqlalchemy_db=db)
manager.create_api(users,primary_key='username',methods=['GET','POST','DELETE'])

@app.route('/userauth')
def index():
	return '<h1>running</h1>'