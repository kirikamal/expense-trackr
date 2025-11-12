import mysql.connector
from contextlib import contextmanager
from backend.logger_setup import setup_logger


logger = setup_logger('db_helper')


@contextmanager
def get_db_connection(commit=False):
    """Context manager for database connection."""
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Kiri@1234',
        database='expense_manager'
    )

    if conn.is_connected():
        cursor = conn.cursor(dictionary=True)
        try:
            yield cursor
            if commit:
                conn.commit()
        finally:
            cursor.close()
            conn.close()


def fetch_all_records():
    logger.info(f"Fetching all records from the database.")
    with get_db_connection() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        return expenses


def fetch_expenses_for_date(expense_date):
    logger.info(f"Fetching expenses for date: {expense_date}")
    with get_db_connection() as cursor:
        query = "SELECT * FROM expenses WHERE expense_date = %s"
        cursor.execute(query, (expense_date,))
        results = cursor.fetchall()
        return results


def fetch_expense_summary(start_date, end_date):
    logger.info(f"Fetching expense summary from {start_date} to {end_date}")
    with get_db_connection() as cursor:
        query = """
            SELECT category, SUM(amount) AS total_amount
            FROM expenses
            WHERE expense_date BETWEEN %s AND %s
            GROUP BY category
        """
        cursor.execute(query, (start_date, end_date))
        results = cursor.fetchall()
        return results

def insert_expense(category, amount, expense_date, notes):
    logger.info(f"Inserting expense: {category}, {amount}, {expense_date}, {notes}")
    with get_db_connection(commit=True) as cursor:
        query = """
            INSERT INTO expenses (category, amount, expense_date, notes)
            VALUES (%s, %s, %s,%s)
        """
        cursor.execute(query, (category, amount, expense_date, notes))


def delete_expense(expense_date):
    logger.info(f"Deleting expenses for date: {expense_date}")
    with get_db_connection(commit=True) as cursor:
        query = "DELETE FROM expenses WHERE expense_date = %s"
        cursor.execute(query, (expense_date,))


def fetch_monthly_expense_summary():
    logger.info(f"Fetch expense summary by month")
    with get_db_connection() as cursor:
        query = """
            SELECT month(expense_date) as expense_month,
            monthname(expense_date) as month_name,
            sum(amount) as total
            FROM expenses
            GROUP BY expense_month, month_name
        """

        cursor.execute(query)
        expenses = cursor.fetchall()
        return expenses


if __name__ == '__main__':
    # Example usage
    # insert_expense('Food', 15.50, '2024-06-01', 'Lunch at cafe')
    # fetch_all_records()
    # fetch_expenses_for_date('2024-08-02')
    # results = fetch_expense_summary('2024-08-01', '2024-08-30')
    # for res in results:
    #     print(res)
    # delete_expense('2024-06-01')
    print(fetch_monthly_expense_summary())
