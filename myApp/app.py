from flask import current_app
from flask import Flask
from flask_mysqldb import MySQL
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dbs_ptsd'
mysql  = MySQL(app)
app.secret_key = 'secret'

from myApp.controllers.ptsd import (
    index as idx,
    login as lgn,
    register as rgt,
    admin as adm,
    logout as lgt
)



@app.route('/')
def index():
    return idx()

@app.route('/admin')
def admin():
    return adm()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return lgn()

@app.route('/register', methods=['GET', 'POST'])
def register():
    return rgt()

@app.route('/logout')
def logout():
    return lgt()