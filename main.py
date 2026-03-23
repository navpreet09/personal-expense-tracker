from repository import ExpenseRepository

repo = ExpenseRepository()

print("1. Add expense")
print("2. View expenses")
print("3. Generate monthly total")
print("4. Filter expenses by category")
print("5. Send monthly summary")

choice = input("Choose an option: ")