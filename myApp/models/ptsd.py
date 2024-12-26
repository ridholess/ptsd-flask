from myApp.app import mysql
from werkzeug.security import check_password_hash, generate_password_hash

def getUserByEmail(email):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM user WHERE email = %s", (email,))
        user = cursor.fetchone()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        user = None
    finally:
        cursor.close()
    return user

def verifyPassword(hashedPassword, password):
        return check_password_hash(hashedPassword, password)
    
def createUser(nama, email, password):
    hashedPassword = generate_password_hash(password)
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO user (nama, email, password) VALUES (%s, %s, %s)",
                (nama, email, hashedPassword))
    mysql.connection.commit()
    cursor.close()
    
def getAllQuestions():
    print("get_all_questions dipanggil.")
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM questions"
    cursor.execute(query)
    questions = cursor.fetchall()
    cursor.close()
    return questions

def saveTotalScore(user_id, score):
    """
    Menyimpan jawaban pengguna ke tabel `user_scores`.

    Args:
        user_id (int): ID pengguna.
        question_id (int): ID pertanyaan.
        user_answer (str): Jawaban pengguna ('agree', 'neutral', 'disagree').
        score (int): Skor jawaban berdasarkan bobot.
    """
    cursor = mysql.connection.cursor()
    cursor = mysql.connection.cursor()
    query = """
        INSERT INTO user_scores (user_id, score)
        VALUES (%s, %s)
    """
    cursor.execute(query, (user_id, score))
    mysql.connection.commit()
    cursor.close()

def getQuestionWeights(question_id):
    """
    Mengambil bobot skor untuk setiap jawaban dari tabel `questions`.
    """
    cursor = mysql.connection.cursor()
    query = """
        SELECT weight_disagree, weight_neutral, weight_agree
        FROM questions WHERE id = %s
    """
    cursor.execute(query, (question_id,))
    weights = cursor.fetchone()
    cursor.close()

    if weights:
        return {
            'disagree': weights[0] if weights[0] is not None else 0,
            'neutral': weights[1] if weights[1] is not None else 0,
            'agree': weights[2] if weights[2] is not None else 0
        }
    else:
        # Kembalikan default jika tidak ada data
        return {'agree': 0, 'neutral': 0, 'disagree': 0}
    return {}

def saveTestResult(user_id, score, status):
    """
    Menyimpan hasil tes baru ke tabel `user_scores`.

    Args:
        user_id (int): ID pengguna.
        score (int): Total skor dari tes.
    """
    cursor = mysql.connection.cursor()
    query = """
        INSERT INTO user_scores (user_id, score, status)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (user_id, score, status))
    mysql.connection.commit()
    test_id = cursor.lastrowid  # Dapatkan ID hasil tes terakhir
    cursor.close()
    return test_id

def getUserTestResults(user_id):
    """
    Mengambil semua hasil tes dari pengguna berdasarkan user_id.

    Args:
        user_id (int): ID pengguna.

    Returns:
        list: Daftar hasil tes.
    """
    cursor = mysql.connection.cursor()
    query = """
        SELECT *
        FROM user_scores
        WHERE user_id = %s
        ORDER BY created_at DESC
    """
    cursor.execute(query, (user_id,))
    results = cursor.fetchall()
    cursor.close()
    return results