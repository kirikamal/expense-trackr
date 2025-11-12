import streamlit as st
from expense_save_tab import save_expenses_tab


st.title("Expense Trackr")

tab1, tab2, tab3 = st.tabs(["Add/Update Expenses", "Analytics By Category", "Analytics By Months"])

with tab1:
    save_expenses_tab()

with tab2:
    st.write("Analytics By Category - Coming Soon!")

with tab3:
    st.write("Analytics By Months - Coming Soon!")