# base.py
import sqlite3

class BaseORM:
    db_name = "football_management.db"

    def __init__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        raise NotImplementedError("Subclasses should implement this!")

    def commit_and_close(self):
        self.conn.commit()
        self.conn.close()

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor

    def create(self, query, params):
        self.execute_query(query, params)
        self.commit_and_close()

    def delete(self, query, params):
        self.execute_query(query, params)
        self.commit_and_close()

    def find_all(self, query):
        return self.execute_query(query).fetchall()

    def find_by_id(self, query, params):
        return self.execute_query(query, params).fetchone()


