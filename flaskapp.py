#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: flaskapp.py
# @Created:   2018-04-17 00:09:27  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-17 02:08:16  Simon Seo (simon.seo@nyu.edu)
from flask import Flask, request, render_template, redirect, url_for

# Built-in
import os

# Private Libs
import psycopg2

# My own
from form import RegistrationForm, PasscodeRequestForm


app = Flask(__name__)
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

@app.route("/")#, methods=['GET','POST'])
def main():
	return '''
	<!doctype html>
	<title>Input new </title>
	<h1>Upload new File</h1>
	'''

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    # your code
    # return a response
    # 

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        # db_session.add(user) # SQLAlchemy
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/generate-passocde', methods=['GET', 'POST'])
def generate_passcode():
    form = PasscodeRequestForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        # db_session.add(user) # SQLAlchemy
        flash('We\'ll send you an email with your new passcode!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=int(os.environ["PORT"]))

	


