#!/usr/bin/python3

from flask import Flask
from flask import render_template
from flask import url_for
from flask import request, redirect
from flask import session
from flask import flash
from functools import wraps

#create application object
app = Flask(__name__)

#creating a secret key for app
app.secret_key = "my cloud secret key"

#login required decorator
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash("Please login first.")
			return redirect(url_for('login'))
	return wrap

@app.route('/')
@login_required
def home():
    return render_template("index.html")

@app.route('/welcome')
def welcome():
	return render_template("welcome.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	error= None
	if request.method == 'POST':
		if request.form['username'] != 'demo' or request.form['password'] != 'demo':
			error = 'Invalid login, Please try again.'
		else:
			session['logged_in']= True
			flash ('You are logged in to My Cloud!')
			return redirect(url_for('home'))
	return render_template('login.html', error=error)
	
@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in',None)
	flash ('You are logged out from My Cloud!')
	return redirect(url_for('welcome'))


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)
