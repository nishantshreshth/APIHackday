from flask import Flask,render_template, redirect, url_for, request, json, session, make_response
import pymongo
from bson.objectid import ObjectId
import os,sys

app = Flask(__name__)
#connection = pymongo.MongoClient("mongodb://localhost")
#connection = pymongo.MongoClient("mongodb://localhost")
#db= connection['TeleDoc']        



app.secret_key="cvsa213526bcdmdhdjGFF2324vF342fGtYHj42"

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	return "login"

'''
@app.route('/signup', methods=['GET', 'POST'])
def signUp():
	return render_template('signup.html')
'''

if __name__ == '__main__':
	app.run(debug=True)
