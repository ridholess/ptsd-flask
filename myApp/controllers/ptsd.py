from flask import Blueprint, render_template, request, redirect, url_for, flash
import mysql.connector
# from myApp.models.ptsd import PTSD


auth_bp = Blueprint('auth', __name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dbs_ptsd"
    )

def index():
    return render_template('index.html')
def admin():
    return render_template('admin.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query to check if the user exists
        cursor.execute("SELECT * FROM user WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()

        # Authentication check
        if user:
            flash('Login successful!', 'success')
            return redirect(url_for('admin'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')

        # Close the connection
        cursor.close()
        conn.close()

    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        nama = request.form['nama']
        password = request.form['password']
        created_at = request.form['created_at']

        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query to insert the user
        cursor.execute("INSERT INTO user (email, nama, password, created_at) VALUES (%s, %s, %s)", (email, nama, password, created_at))
        conn.commit()

        flash('Registration successful! You can now log in.', 'success')

        # Close the connection
        cursor.close()
        conn.close()

        return redirect(url_for('admin'))

    return render_template('register.html')