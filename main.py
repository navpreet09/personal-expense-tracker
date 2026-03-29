from repository import ExpenseRepository
from models import Expense
from strategies import MonthlySummaryStrategy, TotalSummaryStrategy
from email_service import EmailService

repo = ExpenseRepository()
repo.create_table()
email_service = EmailService()

print("1. Add expense")
print("2. View expenses")
print("3. Generate monthly total")
print("4. Filter expenses by category")
print("5. Send total summary email")

choice = input("Choose an option: ")

if choice == "1":
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    expense = Expense(amount, category, date)
    repo.add_expense(expense)

    print("Expense added successfully.")

elif choice == "2":
    expenses = repo.get_all_expenses()

    if not expenses:
        print("No expenses found.")
    else:
        print("\nYour expenses:")
        for e in expenses:
            print(f"Amount: {e.amount}, Category: {e.category}, Date: {e.date}")

elif choice == "3":
    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year (YYYY): "))

    expenses = repo.get_expenses_by_month(month, year)

    if not expenses:
        print("No expenses found for this month.")
    else:
        strategy = MonthlySummaryStrategy()
        summary = strategy.generate_summary(expenses)

        print("\nMonthly total:")
        print(summary)

elif choice == "4":
    category = input("Enter category to filter: ")

    expenses = repo.get_expenses_by_category(category)

    if not expenses:
        print("No expenses found for this category.")
    else:
        print("\nFiltered expenses:")
        for e in expenses:
            print(f"Amount: {e.amount}, Category: {e.category}, Date: {e.date}")

elif choice == "5":
    print("Choose summary type:")
    print("1. Total summary")
    print("2. Monthly summary")

    summary_choice = input("Enter choice: ")

    if summary_choice == "1":
        expenses = repo.get_all_expenses()
        strategy = TotalSummaryStrategy()

    elif summary_choice == "2":
        month = int(input("Enter month (1-12): "))
        year = int(input("Enter year (YYYY): "))
        expenses = repo.get_expenses_by_month(month, year)
        strategy = MonthlySummaryStrategy()

    else:
        print("Invalid choice.")
        exit()

    if not expenses:
        print("No expenses available.")
    else:
        summary = strategy.generate_summary(expenses)

        print("\nSummary:")
        print(summary)

        email = input("Enter email to send summary: ")
        email_service.send_summary(email, summary)

else:
    print("Invalid choice.")