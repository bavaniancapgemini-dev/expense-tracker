from expense import show_expenses
from storage import save_expenses, load_expenses
from utils import title
from report import total_expense


expenses = load_expenses()


while True:

    title()

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Choose: ")


    if choice == "1":

        name = input("Expense Name: ")

        amount = input("Amount: ")

        expense = name + "-" + amount

        expenses.append(expense)

        save_expenses(expenses)

        print("Expense Added")


    elif choice == "2":

        show_expenses(expenses)


    elif choice == "3":

        total = total_expense(expenses)

        print("Total Expense:", total)


    elif choice == "4":

        break


    else:

        print("Invalid Choice")