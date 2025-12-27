# Expense Trackr

This project is an Expense Tracking Application created with Python FastAPI backend and a Streamlit frontend.


## Project Structure
- `backend/`: Contains the FastAPI backend code, including database interactions and API endpoints.
- `frontend/`: Contains the Streamlit frontend code for user interaction.
- `tests/`: Contains unit tests for both backend and frontend components.

### Requirements
- `requirements.txt`: Lists all Python dependencies for the project.

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/kirikamal/expense-trackr.git
   cd expense-trackr
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Database**:

   Update the database connection settings in `backend/db_helper.py` with your MySQL credentials (<YOUR_DB_USER_NAME> & <YOUR_DB_PASSWORD>).
   And use the database schema from `database/expense_manager_expenses.sql` to set up your database.

4. **Run the projet with one command**:

    ```
    bash run.sh
    ```

5. **Run backend & frontend separately**

   5.1. **Run backend from root directory**:

   ```commandline
    python3 -m uvicorn backend.server:app --reload
    ```

   5.2. **Run frontend from root directory**:

    ```commandline
    python3 -m streamlit run frontend/app.py
    ```

## Running Tests
To run the tests, use the following command from the root directory:

    ```bash
    pytest -v
    ```