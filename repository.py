from db_connect import conn
from models import Expense

class ExpenseRepository:

    def create_table(self):
        try:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id SERIAL PRIMARY KEY,
                    amount DECIMAL NOT NULL,
                    category VARCHAR(50),
                    date DATE
                )
            """)
            conn.commit()
            cur.close()
        except Exception as e:
            print("Database error (create_table):", e)

    def add_expense(self, expense):
        try:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO expenses (amount, category, date) VALUES (%s, %s, %s)",
                (expense.amount, expense.category, expense.date)
            )
            conn.commit()
            cur.close()
        except Exception as e:
            print("Database error (add_expense):", e)

    def get_all_expenses(self):
        try:
            cur = conn.cursor()
            cur.execute("SELECT amount, category, date FROM expenses")
            rows = cur.fetchall()

            expenses = []
            for row in rows:
                expenses.append(Expense(row[0], row[1], row[2]))

            cur.close()
            return expenses

        except Exception as e:
            print("Database error (get_all_expenses):", e)
            return []

    def get_expenses_by_category(self, category):
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT amount, category, date FROM expenses WHERE category = %s",
                (category,)
            )

            rows = cur.fetchall()

            expenses = []
            for row in rows:
                expenses.append(Expense(row[0], row[1], row[2]))

            cur.close()
            return expenses

        except Exception as e:
            print("Database error (get_expenses_by_category):", e)
            return []

    def get_expenses_by_month(self, month, year):
        try:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT amount, category, date
                FROM expenses
                WHERE EXTRACT(MONTH FROM date) = %s
                AND EXTRACT(YEAR FROM date) = %s
                """,
                (month, year)
            )

            rows = cur.fetchall()

            expenses = []
            for row in rows:
                expenses.append(Expense(row[0], row[1], row[2]))

            cur.close()
            return expenses

        except Exception as e:
            print("Database error (get_expenses_by_month):", e)
            return []