import sqlite3
from db import DB


class UsersModel(DB):

    def __init__(self, arg):
        self.connection = sqlite3.connect('templates/users1.db', check_same_thread=False)

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users1 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             user_name VARCHAR(50),
                             password_hash VARCHAR(128),
                             flag bit NULL DEFAULT 0
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, user_name, password_hash):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users1 
                          (user_name, password_hash) 
                          VALUES (?,?)''', (user_name, password_hash))
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users1 WHERE id = ?", (str(user_id),))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users1")
        rows = cursor.fetchall()
        return rows

    def exists(self, user_name, password_hash):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users1 WHERE user_name = ? AND password_hash = ?",
                       (user_name, password_hash))
        row = cursor.fetchone()
        return (True, row[0]) if row else (False,)
