import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"

def save_expenses_tab():
    selected_date = st.date_input("Select Date", datetime(2025, 11, 10), label_visibility="collapsed")
    # Use ISO date string when contacting API and for widget keys
    date_str = selected_date.isoformat() if hasattr(selected_date, 'isoformat') else str(selected_date)
    response = requests.get(f"{API_URL}/expenses/{date_str}")

    if response.status_code == 200:
        existing_expenses = response.json()
    else:
        st.error("Failed to retieve expenses.")
        existing_expenses = []

    categories = ["Food", "Rent", "Shopping", "Entertainment", "Others"]

    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")

        expenses_entries = []

        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i]['amount']
                category = existing_expenses[i]['category']
                notes = existing_expenses[i]['notes']
            else:
                amount = 0.0
                category = categories[0]
                notes = ""

            col1, col2, col3 = st.columns(3)

            # include date_str in keys so Streamlit treats widgets for each date separately
            with col1:
                amount_input = st.number_input(
                    label="Amount",
                    min_value=0.0,
                    step=1.0,
                    value=amount,
                    key=f"amount_{date_str}_{i}",
                    label_visibility="collapsed",
                )
            with col2:
                # safe index lookup in case category returned isn't in our local list
                selected_index = categories.index(category) if category in categories else 0
                category_input = st.selectbox(
                    label="Category",
                    options=categories,
                    index=selected_index,
                    key=f"category_{date_str}_{i}",
                    label_visibility="collapsed",
                )
            with col3:
                notes_input = st.text_input(
                    label="Notes",
                    value=notes,
                    key=f"notes_{date_str}_{i}",
                    label_visibility="collapsed",
                )

            expenses_entries.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })

        submit_button = st.form_submit_button()
        if submit_button:
            filtered_expenses = [expense for expense in expenses_entries if expense['amount'] > 0]

            response = requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)

            if response.status_code == 200:
                st.success("Expenses saved successfully!")
            else:
                st.error("Failed to save expenses.")
