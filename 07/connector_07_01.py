"""1) Написать контекстный менеджер для работы с SQLite DB"""
import sqlite3


class DBConnect:

    def __init__(self, db_name):
        self._db_name = db_name
        self._conn = None

    def __enter__(self):
        self._conn = sqlite3.connect(self._db_name)
        return self._conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.close()
