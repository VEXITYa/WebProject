import sqlite3
from db import DB


class NewsModel(DB):

    def __init__(self, arg):
        self.connection = sqlite3.connect('templates/news.db', check_same_thread=False)

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS news 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             title VARCHAR(100),
                             content VARCHAR(1000),
                             user_id INTEGER,
                             news_time INTEGER
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, title, content, user_id, time):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO news 
                          (title, content, user_id, news_time) 
                          VALUES (?,?,?,?)''', (title, content, str(user_id), time))
        cursor.close()
        self.connection.commit()

    def get(self, news_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM news WHERE id = ? ORDER BY news_time DESC", (str(news_id),))
        row = cursor.fetchone()
        return row

    def get_all(self, user_id=None):
        cursor = self.connection.cursor()
        if user_id:
            cursor.execute("SELECT * FROM news WHERE user_id = ? ORDER BY news_time DESC",
                           (str(user_id),))
        else:
            cursor.execute("SELECT * FROM news ORDER BY news_time DESC")
        rows = cursor.fetchall()
        return rows

    def delete(self, news_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM news WHERE id = ? ''', (str(news_id),))
        cursor.close()
        self.connection.commit()
