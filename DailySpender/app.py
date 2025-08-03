import sqlite3 as db
import datetime
conn = db.connect('database.db')
c = conn.cursor()

def create_table():
    # intial database
    c.execute('''CREATE TABLE IS NOT EXISTS expenses (
                 amount REAL,
                 category TEXT COLLATE NOCASE,
                 message TEXT,
                 date TEXT
                 )
                 ''')
    conn.commit()
    conn.close()
    
def add(amount, category, message, date):
    # add to database
    date = str(datetime.now().strftime('%y - %m - %d | %H:%M'))
    c.execute("INSERT INTO expenses VALUES (:amount, :category, :message , :date)", {
        'amount': amount,
        'category': category,
        'message': message,
        'date': date
    })
    conn.commit()
    conn.close()