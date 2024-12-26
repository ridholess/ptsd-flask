from flask import render_template, request, redirect, url_for, session, flash, current_app
from werkzeug.utils import secure_filename
import os
# from myApp.models.ptsd import PTSD

from myApp.models.ptsd import (
    getUserByEmail,
    verifyPassword,
    createUser,
    getAllQuestions,
    saveTotalScore,
    getQuestionWeights,
    saveTestResult,
    getUserTestResults
    
)

def index():
    if 'id_user' in session:
        user_id = session.get('id_user')
        test_id = request.args.get('test_id')  # Ambil test_id dari query parameter
        results = getUserTestResults(user_id)
        current_result = None
        if test_id:
            current_result = next((result for result in results if result[0] == int(test_id)), None)
        
        return render_template('index.html', results=results, current_result=current_result)
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
            return redirect(url_for('index'))
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

def deteksi():
    if 'id_user' in session:
        user_id = session.get('id_user')
        test_id = request.args.get('test_id')  # Ambil test_id dari query parameter
        results = getUserTestResults(user_id)
        current_result = None
        if test_id:
            current_result = next((result for result in results if result[0] == int(test_id)), None)
    
    questions = getAllQuestions()
    
    return render_template('deteksi.html', questions=questions, results=results, current_result=current_result)

def statusPtsd(total_score):
    if total_score < 20:
        return "Tidak ada gejala"
    elif 20 <= total_score < 65:
        return "Ada sedikit gejala PTSD"
    else:
        return "Gejala PTSD kuat"

def submit_test():
    user_id = session.get('id_user')  # Ambil user ID dari session
    if not user_id:
        flash('Anda harus login terlebih dahulu!', 'danger')
        return redirect(url_for('login'))

    questions = getAllQuestions()  # Ambil semua pertanyaan dari database
    total_score = 0

    for question in questions:
        question_id = question[0]
        user_answer = request.form.get(f'q{question_id}')  # Ambil jawaban pengguna
        if user_answer:
            weights = getQuestionWeights(question_id)
            score = weights.get(user_answer, 0)
            total_score += score
        else:
            flash(f'Pertanyaan {question_id} belum dijawab!', 'danger')

    status = statusPtsd(total_score)
    
    test_id = saveTestResult(user_id, total_score, status)

    # Alihkan ke halaman hasil dengan ID tes
    flash('Tes selesai! Total skor Anda telah disimpan.', 'success')
    return redirect(url_for('result_page', test_id=test_id))

def result_page(test_id):
    user_id = session.get('id_user')
    if not user_id:
        flash('Anda harus login untuk melihat hasil tes!', 'danger')
        return redirect(url_for('login'))

    results = getUserTestResults(user_id)  # Ambil semua hasil tes pengguna
    current_result = next((result for result in results if result[0] == test_id), None)

    if not current_result:
        flash('Hasil tes tidak ditemukan!', 'danger')
        return redirect(url_for('index'))

    return render_template('result.html', current_result=current_result, results=results)

def logout():
    session.pop('id_user', None)
    session.pop('nama', None)
    session.pop('email', None)
    flash('Anda telah keluar.', 'success')
    
    return redirect(url_for('index'))