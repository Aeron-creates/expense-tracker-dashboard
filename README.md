Personal Expense Tracker & Analytics

A phone-built Python project that stores expenses in SQLite and analyzes them with pandas. The planned next stage is an interactive Streamlit dashboard.

Features

- Add and persist expenses using SQLite.
- View transactions and total spending.
- Summarize spending by category.
- Filter expenses above or at/below ₹100.
- Analyze average, highest, and lowest expenses using pandas.
- Calculate category-wise spending percentages.

Initial Findings

The initial dataset contains two expenses:

Category| Amount| Share
Food| ₹50| 50%
Transport| ₹50| 50%
Total| ₹100| 100%

The average expense is ₹50. Both the highest and lowest recorded expenses are ₹50.

These findings describe only the two currently recorded transactions and should not be treated as a long-term spending pattern.

Technology Stack

- Python
- SQLite
- pandas
- Streamlit (planned)

Run Locally

Run the tracker with "python expense_tracker.py" and analyze the database with "python analyze_expenses.py".

The SQLite database is stored locally in "expenses.db".
