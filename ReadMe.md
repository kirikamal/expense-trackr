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

3. **Run backend from root directory**:

    ```commandline
    uvicorn backend.server:app --reload
    ```

4. **Run frontend from root directory**:

    ```commandline
    streamlit run frontend/app.py
    ```

## Running Tests
To run the tests, use the following command from the root directory:

    ```bash
    pytest -v
    ```