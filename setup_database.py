import sqlite3

connection = sqlite3.connect("expenses.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        amount REAL NOT NULL CHECK (amount >= 0),
        category TEXT NOT NULL,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
""")

connection.commit()
connection.close()

print("Database created successfully!")
