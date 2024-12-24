from flask import Flask
from flask_mysqldb import MySQL
from myApp.controllers.ptsd import auth_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dbs_ptsd'
mysql  = MySQL(app)
app.secret_key = 'secret'

from myApp.controllers.ptsd import index as idx, login as lgn, register as rgt, admin as adm

@app.route('/')
def index():
    return idx()

@app.route('/admin')
def admin():
    return adm()

@app.route('/login')
def login():
    return lgn()

@app.route('/register')
def register():
    return rgt()