import sqlite3

def connect_db():
    return sqlite3.connect("expenses.db")

def add_expense():
    name = input("Enter expense name: ").strip()

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount < 0:
                print("Amount cannot be negative.")
                continue

            break
        except ValueError:
            print("Please enter a valid number.")

    category = input("Enter category: ").strip()

    if not name or not category:
        print("Name and category cannot be empty.")
        return

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """INSERT INTO expenses (name, amount, category)
           VALUES (?, ?, ?)""",
        (name, amount, category)
    )

    connection.commit()
    connection.close()

    print("Expense saved permanently!")

def view_expenses():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, name, amount, category FROM expenses"
    )

    expenses = cursor.fetchall()
    connection.close()

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n========== YOUR EXPENSES ==========")

    for expense in expenses:
        print(
            f"ID: {expense[0]} | "
            f"{expense[1]} | "
            f"₹{expense[2]:.2f} | "
            f"{expense[3]}"
        )

    print("===================================")


def view_total():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    result = cursor.fetchone()

    connection.close()

    total = result[0] if result[0] is not None else 0

    print(f"Total spending: ₹{total:.2f}")

def view_category_totals():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
        ORDER BY SUM(amount) DESC
    """)

    results = cursor.fetchall()
    connection.close()

    if not results:
        print("No expenses recorded yet.")
        return

    print("\n========== CATEGORY SUMMARY ==========")

    for category, total in results:
        print(f"{category}: ₹{total:.2f}")

    print("======================================")

def view_expenses_above_100():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, amount, category
        FROM expenses
        WHERE amount > 100
        ORDER BY amount DESC
    """)

    expenses = cursor.fetchall()
    connection.close()

    if not expenses:
        print("No expenses above ₹100 found.")
        return

    for expense in expenses:
        print(
            f"ID: {expense[0]} | "
            f"{expense[1]} | "
            f"₹{expense[2]:.2f} | "
            f"{expense[3]}"
        )

def view_expenses_below_100():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, amount, category
        FROM expenses
        WHERE amount <= 100
        ORDER BY amount DESC
    """)

    expenses = cursor.fetchall()
    connection.close()

    if not expenses:
        print("No expenses at or below ₹100 found.")
        return

    for expense in expenses:
        print(
            f"ID: {expense[0]} | "
            f"{expense[1]} | "
            f"₹{expense[2]:.2f} | "
            f"{expense[3]}"
        )

while True:
    print("\n====================================")
    print("       PERSONAL EXPENSE TRACKER")
    print("====================================")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View total spending")
    print("4. View category-wise spending")
    print("5. View expenses above ₹100")
    print("6. View expenses below ₹100")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        view_total()

    elif choice == "4":
        view_category_totals()

    elif choice == "5":
        view_expenses_above_100()

    elif choice == "6":
        view_expenses_below_100()

    elif choice == "7":
        print("Thank you for using Personal Expense Tracker!")
        break    
    else:
        print("Invalid choice. Please select 1-7.")
