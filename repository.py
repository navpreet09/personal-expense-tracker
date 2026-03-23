from db_connect import conn
from models import Expense

class ExpenseRepository:

    def add_expense(self, expense):
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO expenses (amount, category, date) VALUES (%s, %s, %s)",
            (expense.amount, expense.category, expense.date)
        )

        conn.commit()
        cur.close()

    def get_all_expenses(self):
        cur = conn.cursor()

        cur.execute("SELECT amount, category, date FROM expenses")
        rows = cur.fetchall()

        expenses = []
        for row in rows:
            expense = Expense(row[0], row[1], row[2])
            expenses.append(expense)

        cur.close()
        return expenses