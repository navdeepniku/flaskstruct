#!/usr/bin/python3

from flask import Flask

#create application object
app = Flask(__name__)

from flaskstruct.dbconnect import connection


#creating a secret key for app
app.secret_key = "my cloud secret key"

from flaskstruct import routes