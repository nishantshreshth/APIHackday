from flask import Flask,render_template, redirect, url_for, request, json, session, make_response
import pymongo
import sendgrid
from bson.objectid import ObjectId
import os,sys

app = Flask(__name__)
connection = pymongo.MongoClient("mongodb://localhost")
db= connection['TeleDoc']
nUser= db.newUsers        
faq=db.FAQs
nq=db.newQues


app.secret_key="cvsa213526bcdmdhdjGFF2324vF342fGtYHj42"

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('index.html')


@app.route('/ngo', methods=['GET', 'POST'])
def login():
	if request.method== 'POST':
		dt={}
		q=request.form['q']
		print q
		qlist=q.split()
		for item in faq.find():
			for ch in qlist:
				if ch in item['ques']:
					dt[ques]

	return render_template('ngo.html')

@app.route('/addQues', methods=['GET', 'POST'])
def addQues():
	if request.method =='POST':
		print "Hello"
		name=request.form['name']
		print name
		ph=request.form['phone']
		print ph
		q=request.form['ques']
		print q
		stri="<b>Name : </b>"+name+"<br/>"+"<b>Contact : </b>"+ph+"<br/>"+"<b>Problem: </b>"+q
		print stri
		sg = sendgrid.SendGridClient("AnujDuggal21","UniverSe@3")
		message = sendgrid.Mail()
		message.add_to("er.anujduggal@gmail.com")
		message.set_from("nishantshreshth.13@gmail.com")
		message.set_subject("Urgent: New Query From Patient")
		message.set_html(stri)
		k=sg.send(message)
		print k
		return "Question Submitted"
	else:
		return render_template('newQA.html')

@app.route('/getCall', methods=['GET', 'POST'])
def call():
	print request.args
	id1 = request.args.get('From')
	id2=request.args.get('from')
	if id1!=None:
		return str(id1)+" calling...."
	elif id2!=None:
		return str(id2)+" calling....."
	else:
		return "+917723004424 calling...."

'''
@app.route('/signup', methods=['GET', 'POST'])
def signUp():
	return render_template('signup.html')
'''

if __name__ == '__main__':
	app.run(debug="0.0.0.0")
