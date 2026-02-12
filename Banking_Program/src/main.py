def show_balance():
	print(f"Your Balance is: ${balance:.2f}")


def deposit():
	amount = float(input("Enter amount:"))
	if amount < 0:
		print("That is not a valid deposit")
		return 0
	else:
		return amount

		print("Your Balance is: ", balance)


def withdraw():
	amount = float(input("Enter amount:"))
	if amount < 0:
		print("Amount is not a valid withdraw")
		return 0
	elif amount > balance:
		print("Insufficient funds")
		return 0


	else:
		return amount
		print("Your Balance is: ", balance)


balance = 0
is_running = True
while is_running:
	print('Banking Program')
	print("1.Show Balance")
	print("2.Deposit")
	print("3.Withdraw")
	print("4.Exit")
	choice = input("Enter your choice:")

	if choice == "1":
		show_balance()
	elif choice == "2":
		balance += deposit()

	elif choice == "3":
		balance -= withdraw()

	elif choice == "4":
		is_running = False
	else:
		print("Invalid Choice")
print("Thank You Have a Nice Day")
