
import sqlite3
from pathlib import Path

import pandas as pd
import streamlit as st

DB_PATH = Path(__file__).parent / "expenses.db"

st.set_page_config(
    page_title="Expense Dashboard",
    page_icon="💰",
    layout="wide",
)

st.title("💰 Personal Expense Dashboard")
st.caption("Track spending. Understand your habits.")

@st.cache_data
def load_expenses():
    if not DB_PATH.exists():
        return pd.DataFrame(
            columns=["id", "name", "amount", "category", "created_at"]
        )

    with sqlite3.connect(DB_PATH) as connection:
        return pd.read_sql_query(
            """
            SELECT id, name, amount, category, created_at
            FROM expenses
            ORDER BY created_at DESC
            """,
            connection,
        )

df = load_expenses()

if df.empty:
    st.info("No expenses found. Add demo or personal data to get started.")
    st.stop()

df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
df = df.dropna(subset=["amount"])
total = df["amount"].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Spending", f"₹{total:,.2f}")
col2.metric("Transactions", len(df))
col3.metric(
    "Average Expense",
    f"₹{df['amount'].mean():,.2f}" if not df.empty else "₹0.00",
)

st.subheader("Category-wise Spending")
category_totals = (
    df.groupby("category", as_index=False)["amount"]
    .sum()
    .sort_values("amount", ascending=False)
)

if not category_totals.empty:
    st.bar_chart(category_totals, x="category", y="amount")
    st.dataframe(category_totals, use_container_width=True, hide_index=True)

st.subheader("All Transactions")
st.dataframe(df, use_container_width=True, hide_index=True)
