from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import date
from . import db_helper

app = FastAPI()

class Expense(BaseModel):
    category: str
    amount: float
    notes: str


class DateRange(BaseModel):
    start_date: date
    end_date: date


@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from the database")

    return expenses


@app.post("/expenses/{expense_date}")
def save_expense(expense_date: date, expenses: list[Expense]):
    try:
        for expense in expenses:
            db_helper.insert_expense(expense.category, expense.amount, expense_date, expense.notes)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Failed to save expenses: {str(ex)}")

    return {"message": "Expenses saved successfully"}


@app.get("/monthly_summary/")
def get_monthly_summary():
    summary = db_helper.fetch_monthly_expense_summary()
    if summary is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve monthly summary from the database")

    return summary


@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    summary = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if summary is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database")

    total = sum([row['total'] for row in summary])

    breakdown = {}
    for row in summary:
        percentage = (row['total']/total)*100 if total > 0 else 0
        breakdown[row['category']] = {
            'total': row['total'],
            'percentage': percentage
        }

    return breakdown