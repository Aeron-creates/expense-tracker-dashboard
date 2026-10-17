import sqlite3
import pandas as pd

# Connect to our database
connection = sqlite3.connect("expenses.db")

# Load expenses into a DataFrame
df = pd.read_sql_query(
    "SELECT id, name, amount, category, created_at FROM expenses",
    connection
)

connection.close()

if df.empty:
    print("No expenses recorded yet.")

else:
    print("\n========== EXPENSE ANALYSIS ==========")

    # Basic statistics
    print(f"\nTotal expenses: {len(df)}")
    print(f"Total spending: ₹{df['amount'].sum():.2f}")
    print(f"Average expense: ₹{df['amount'].mean():.2f}")
    print(f"Highest expense: ₹{df['amount'].max():.2f}")
    print(f"Lowest expense: ₹{df['amount'].min():.2f}")

    # Category analysis
    print("\n------ CATEGORY-WISE SPENDING ------")

    category_totals = (
        df.groupby("category")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    for category, total in category_totals.items():
        percentage = total / df["amount"].sum() * 100

        print(
            f"{category}: ₹{total:.2f} "
            f"({percentage:.1f}%)"
        )

    # Display all records
    print("\n------ ALL EXPENSES ------")
    print(df.to_string(index=False))

    print("\n====================================")
