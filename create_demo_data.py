
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "expenses.db"

sample_expenses = [
    ("Breakfast", 60, "Food", "2026-10-14 08:30:00"),
    ("Bus fare", 40, "Transport", "2026-10-14 09:00:00"),
    ("Lunch", 120, "Food", "2026-10-14 13:00:00"),
    ("Notebook", 75, "Education", "2026-10-15 11:00:00"),
    ("Mobile recharge", 199, "Bills", "2026-10-15 18:00:00"),
    ("Dinner", 100, "Food", "2026-10-16 20:00:00"),
    ("Auto fare", 90, "Transport", "2026-10-16 21:00:00"),
]

with sqlite3.connect(DB_PATH) as connection:
    connection.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL CHECK (amount >= 0),
            category TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.execute("DELETE FROM expenses")

    connection.executemany("""
        INSERT INTO expenses (name, amount, category, created_at)
        VALUES (?, ?, ?, ?)
    """, sample_expenses)

print(f"Demo database created: {DB_PATH}")
print(f"Sample transactions added: {len(sample_expenses)}")
