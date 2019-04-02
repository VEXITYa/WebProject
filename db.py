import sqlite3


class DB:

    def __init__(self):
        self.connection = sqlite3.connect('news.db', check_same_thread=False)

    def get_connection(self):
        return self.connection

    def __del__(self):
        self.connection.close()
