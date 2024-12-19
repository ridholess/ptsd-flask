from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dbs_ptsd'
mysql  = MySQL(app)
app.secret_key = 'secret'

from myApp.controllers.ptsd import index as idx

@app.route('/')
def index():
    return idx()