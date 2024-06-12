import sqlite3

CONN = sqlite3.connect("db/footballmanagement.db")
CURSOR = CONN.cursor()
