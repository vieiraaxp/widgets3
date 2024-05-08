import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('users.db')
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (email TEXT, password TEXT);''')
    except sqlite3.Error as e:
        print(e)

def add_user(conn, email, password):
    sql = '''INSERT INTO users(email,password) VALUES(?,?);'''
    cur = conn.cursor()
    cur.execute(sql, (email, password))
    conn.commit()
    return cur.lastrowid

def validate_user(conn, email, password):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email=(?) AND password=(?);", (email, password))
    row = cur.fetchone()
    return row is not None

connection = create_connection()
create_table(connection)

add_user(connection, 'user@example.com', 'password123')

email = 'user@example.com'
password = 'password123'
if validate_user(connection, email, password):
    print(f"Usuário {email} logado com sucesso!")
else:
    print("Email ou senha inválidos.")