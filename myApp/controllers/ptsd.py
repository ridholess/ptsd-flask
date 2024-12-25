from flask import render_template, request, redirect, url_for, session, flash, current_app
from werkzeug.utils import secure_filename
import os
# from myApp.models.ptsd import PTSD

from myApp.models.ptsd import (
    getUserByEmail,
    verifyPassword,
    createUser
)

def index():
    return render_template('index.html')

def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = getUserByEmail(email)
        
        if user and verifyPassword(user[3], password):
            session['id_user'] = user[0]
            session['nama'] = user[1]
            session['email'] = user[2]
            
            flash('Selamat datang!', 'success')
            return redirect(url_for('admin'))
        else:
            flash('Gagal masuk. Coba lagi!', 'danger')
    
    return render_template('login.html')

def register():
    if request.method == 'POST':
        email = request.form['email']
        nama = request.form['nama']
        password = request.form['password']

        createUser(nama, email, password)
        
        flash('Berhasil daftar! Silakan login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

def admin():
    if 'id_user' not in session:
        flash('Silakan login terlebih dahulu.', 'warning')
        return redirect(url_for('login'))
    
    return render_template('admin.html')