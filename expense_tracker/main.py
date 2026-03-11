class Expense:
    def __init__(self, category, amount, description):
        self.category = category
        self.amount = amount
        self.description = description

    def display(self):
        print(f"Category: {self.category} | Amount: ${self.amount} | Note: {self.description}")


class ExpenseTracker:
	def __init__(self):
		self.expenses = []

	# Add expense
	def add_expense(self, expense):
		self.expenses.append(expense)
		print("Expense added successfully!")

	# View all expenses
	def view_expenses(self):
		if not self.expenses:
			print("No expenses recorded.")
			return

		for expense in self.expenses:
			expense.display()

	# Calculate total expense
	def total_expense(self):
		total = sum(expense.amount for expense in self.expenses)
		print(f"Total Expense: ${total}")

tracker = ExpenseTracker()

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")

        expense = Expense(category, amount, description)
        tracker.add_expense(expense)

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        tracker.total_expense()

    elif choice == "4":
        print("Exiting program")
        break

    else:
        print("Invalid choice")