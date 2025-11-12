import streamlit as st
from expense_save_tab import save_expenses_tab
from analytics_ui import analytics_tab
from analytics_by_months import analytics_months_tab


st.title("Expense Trackr")

tab1, tab2, tab3 = st.tabs(["Add/Update Expenses", "Analytics By Category", "Analytics By Months"])

with tab1:
    save_expenses_tab()

with tab2:
    analytics_tab()

with tab3:
    analytics_months_tab()