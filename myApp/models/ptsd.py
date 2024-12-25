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