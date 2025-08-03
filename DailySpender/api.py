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
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
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

def remove(amount, category, message=None):
    conn = get_connection()
    c = conn.cursor()
    if message:
        c.execute(
            "DELETE FROM expenses WHERE amount = ? AND category = ? AND message = ? LIMIT 1",
            (amount, category, message)
        )
    else:
        c.execute(
            "DELETE FROM expenses WHERE amount = ? AND category = ? LIMIT 1",
            (amount, category)
        )
    conn.commit()
    conn.close()

def update(amount_old, category_old, amount_new=None, category_new=None, message_new=None):
    conn = get_connection()
    c = conn.cursor()

    updates = []
    params = []

    if amount_new is not None:
        updates.append("amount = ?")
        params.append(amount_new)
    if category_new is not None:
        updates.append("category = ?")
        params.append(category_new)
    if message_new is not None:
        updates.append("message = ?")
        params.append(message_new)

    if not updates:
        conn.close()
        return False  

    params.extend([amount_old, category_old])

    sql = f"UPDATE expenses SET {', '.join(updates)} WHERE amount = ? AND category = ? LIMIT 1"
    c.execute(sql, params)
    conn.commit()
    conn.close()
    return True
