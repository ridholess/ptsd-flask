from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def create_app():
    
    app = Flask(__name__)
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_PORT'] = 3306
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'dbs_ptsd'
    mysql  = MySQL(app)
    app.secret_key = 'secret'
    # mysql.init_app(app)

    from myApp.controllers import main
    app.register_blueprint(main)

    return app
