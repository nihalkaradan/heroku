from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_restless import APIManager


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'

db = SQLAlchemy(app)

class  users(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(200),unique=True,nullable=False)
	password=db.Column(db.String(200),nullable=False)
class publicb(db.model):
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(200),unique=True,nullable=False)
	message=db.Column(db.String(200),nullable=False)
	sender_id=db.Column(db.Integer,nullable=False)

class privateb(db.model):
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(200),unique=True,nullable=False)
	message=db.Column(db.String(200),nullable=False)
	sender_id=db.Column(db.Integer,nullable=False)
	reciever_id=db.Column(db.Integer,nullable=False)
db.create_all()	



manager=APIManager(app,flask_sqlalchemy_db=db)
manager.create_api(users,primary_key='username',methods=['GET','POST','DELETE'])
manager.create_api(publicb,primary_key='title',methods=['GET','POST','DELETE'])
manager.create_api(privateb,primary_key='title',methods=['GET','POST','DELETE'])

@app.route('/userauth')
def index():
	return '<h1>running</h1>'
