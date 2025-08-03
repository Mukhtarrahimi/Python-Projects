import sqlite3
import datetime

def get_connection():
    return sqlite3.connect('database.db')

def create_table():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
                 amount REAL,
                 category TEXT COLLATE NOCASE,
                 message TEXT,
                 date TEXT
                 )
              ''')
    conn.commit()
    conn.close()

def add(amount, category, message, date=None):
    if date is None:
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO expenses VALUES (?, ?, ?, ?)", (amount, category, message, date))
    conn.commit()
    conn.close()

def show(category=None):
    conn = get_connection()
    c = conn.cursor()
    if category:
        c.execute("SELECT date, amount, message FROM expenses WHERE category = ?", (category,))
        results = c.fetchall()
        c.execute("SELECT sum(amount) FROM expenses WHERE category = ?", (category,))
        total_amount = c.fetchone()[0] or 0
    else:
        c.execute("SELECT date, amount, message FROM expenses")
        results = c.fetchall()
        c.execute("SELECT sum(amount) FROM expenses")
        total_amount = c.fetchone()[0] or 0
    conn.close()
    return total_amount, results
