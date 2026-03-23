from repository import ExpenseRepository
from models import Expense

repo = ExpenseRepository()

print("1. Add expense")
print("2. View expenses")
print("3. Generate monthly total")
print("4. Filter expenses by category")
print("5. Send monthly summary")

choice = input("Choose an option: ")

if choice == "1":
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    expense = Expense(amount, category, date)
    repo.add_expense(expense)

    print("Expense added successfully.")