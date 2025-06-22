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
app.config['MYSQL_DB'] = 'db_ptsd'
mysql  = MySQL(app)
app.secret_key = 'secret'

from myApp.controllers.ptsd import (
    index as idx,
    login as lgn,
    register as rgt,
    logout as lgt,
    deteksi as dtk,
    submit_test as st_test,
    result_page as rslt
)



@app.route('/')
def index():
    return idx()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return lgn()

@app.route('/register', methods=['GET', 'POST'])
def register():
    return rgt()

@app.route('/logout')
def logout():
    return lgt()

@app.route('/deteksi', methods=['GET', 'POST'])
def deteksi():
    return dtk()

@app.route('/submit-test', methods=['GET', 'POST'])
def handle_test_submission():
    return st_test()

@app.route('/result/<int:test_id>')
def result_page(test_id):
    return rslt(test_id)

