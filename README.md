💰 Personal Expense Tracker & Dashboard

A Python-based expense tracking and analytics project built using SQLite, pandas, and Streamlit. This project demonstrates how to store financial transactions, analyze spending patterns, and present insights through an interactive dashboard.

✨ Features

- SQLite database: Store expense records persistently.
- Pandas analytics: Calculate total, average, highest, and lowest expenses.
- Category analysis: Summarize spending and compare categories.
- Interactive dashboard: Display key metrics, a category-wise bar chart, and transaction records.
- Sample dataset: Explore the dashboard using fictional transactions.
- Terminal interface: Add, view, and filter expenses using the Python CLI.

📊 Sample Data Insights

The sample dataset contains seven fictional transactions totaling ₹684.

| Category | Spending | Share |
|---|---:|---:|
| Food | ₹280 | 40.9% |
| Bills | ₹199 | 29.1% |
| Transport | ₹130 | 19.0% |
| Education | ₹75 | 11.0% |
| **Total** | **₹684** | **100%** |

The largest spending category in this sample is Food, followed by Bills.

These findings describe only the demonstration dataset and do not represent real personal spending.

🛠️ Technology Stack

- Python
- SQLite
- pandas
- Streamlit
- Git and GitHub

🚀 Run the Project

Install the dependencies:

pip install -r requirements.txt

Create or reset the fictional demonstration dataset:

python create_demo_data.py

Launch the dashboard:

streamlit run app.py

To use the terminal-based tracker:

python expense_tracker.py

To run the pandas analysis:

python analyze_expenses.py

🔒 Data Privacy

The SQLite database is stored locally. Database files are excluded from Git using ".gitignore".

The demonstration database can be recreated using "create_demo_data.py". That script clears the existing expenses table in the project database before inserting sample records. Do not run it against a database containing records you want to preserve.

☁️ Deployment

The project is structured for deployment using Streamlit Community Cloud and a GitHub repository. Cloud deployment and live dashboard testing are still pending.

🎯 Project Goal

To demonstrate practical Python skills in database operations, data analysis, dashboard development, and version control while building a useful personal finance tool.

---

Built with Python on an Android phone using Termux.
