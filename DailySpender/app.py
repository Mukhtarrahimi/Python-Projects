import sqlite3 as db
conn = db.connect('database.db')
c = conn.cursor()

def create_table():
    c.execute('''CREATE TABLE IS NOT EXISTS expenses (
                 amount REAL,
                 category TEXT COLLATE NOCASE,
                 message TEXT,
                 date TEXT
                 )
                 ''')
    conn.commit()
    conn.close()