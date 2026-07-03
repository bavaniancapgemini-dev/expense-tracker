from expense import show_expenses
from search import search_expense
from storage import save_expenses, load_expenses, export_csv
from utils import title
from report import total_expense, highest_expense, average_expense, category_report, monthly_report, dashboard
from budget import remaining_budget
from datetime import datetime
from colorama import Fore, Style, init
from graph import expense_graph
from ai import ai_insights
from auth import register, login
from database import *
from edit import edit_expense
from sorter import *
from filter import *
from analytics import expense_statistics, sort_expenses, category_analytics

init(autoreset=True)
username = "default_user"

expenses = load_expenses(username)
print("\n========== LOGIN SYSTEM ==========\n")

print("1. Login")
print("2. Register")

auth_choice = input("Choose: ")

username = input("Username: ")

password = input("Password: ")

if auth_choice == "1":

    success = login(username, password)

    if success:

        print("Login Successful")

    else:

        print("Invalid Login")

        exit()

elif auth_choice == "2":

    success = register(username, password)

    if success:

        print("Account Created")

    else:

        print("Username Already Exists")

        exit()

expenses = []
while True:

    title()

    print(Fore.CYAN + "1. Add Expense")
    print(Fore.CYAN + "2. View Expenses")
    print(Fore.CYAN + "3. Total Expense")
    print(Fore.CYAN + "4. Search Expense")
    print(Fore.CYAN + "5. Highest Expense")
    print(Fore.CYAN + "6. Average Expense")
    print(Fore.CYAN + "7. Delete Expense")
    print(Fore.CYAN + "8. Budget Tracker")
    print(Fore.CYAN + "9. Category Report")
    print(Fore.CYAN + "10. Monthly Report")
    print(Fore.CYAN + "11. Export CSV")
    print(Fore.CYAN + "12. Edit Expense")
    print(Fore.MAGENTA + "13. Finance Dashboard")
    print(Fore.BLUE + "14. Expense Graph")
    print(Fore.YELLOW + "15. AI Insights")
    print(Fore.GREEN + "16. Sort Expenses")
    print(Fore.GREEN + "17. Filter By Category")
    print(Fore.BLUE + "18. Search By Date")
    print(Fore.WHITE + "19. Statistics Dashboard")
    print(Fore.WHITE + "20. Category Analytics")
    print(Fore.WHITE + "21. Sort Expenses")
    print(Fore.RED + "22. Exit")

    choice = input("Choose: ")

    if choice == "1":
        
        name = input("Expense Name: ")
        
        amount_input = input("Amount: ")
        
        category = input("Category: ")
        
        try:
            
            amount = float(amount_input)
            
            if amount <= 0:
                
                print("Amount must be positive")
                
                continue
            
        except:
            
            print("Invalid amount")
            
            continue
        
        date = datetime.now().strftime("%Y-%m-%d")
        
        add_expense(username,name,amount,category,date)

        print("Expense Added")
        
        print(Fore.GREEN + "Expense Added Successfully")

    elif choice == "2":
        
        expenses = get_expenses(username)

        show_expenses(expenses)


    elif choice == "3":

        total = total_expense(expenses)

        print("Total Expense:", total)


    elif choice == "4":

        keyword = input("Enter keyword to search: ")

        search_expense(keyword)


    elif choice == "5":

        name, amount = highest_expense(expenses)

        print("Highest Expense:", name, "-", amount)

    elif choice == "6":

        avg = average_expense(expenses)

        print("Average Expense:", avg)

    elif choice == "7":

        show_expenses(expenses)

        index = int(input("Enter expense number to delete: ")) - 1

        if index >= 0 and index < len(expenses):

            expenses.pop(index)

            save_expenses(expenses, username)

            print(Fore.RED + "Expense Deleted")

        else:

            print("Invalid Expense Number")

    elif choice == "8":

        budget = float(input("Enter Monthly Budget: "))

        remaining = remaining_budget(budget, expenses)

        print("Remaining Budget:", remaining)

        if remaining < 0:

            print("⚠ Budget Exceeded")

    elif choice == "9":

        report = category_report(expenses)

        print("Category Report:")

        for category, count in report.items():

            print(f"  {category}: {count}")
            
    elif choice == "10":
        from report import monthly_report

        report = monthly_report(expenses)

        print("Monthly Report:")

        for month, total in report.items():

            print(f"  {month}: {total}")
            
    elif choice == "11":
        

        export_csv(expenses)

    elif choice == "12":

        expenses = get_expenses(username)

        show_expenses(expenses)

        expense_id = int(input("Enter Expense ID To Edit: "))

        name = input("New Name: ")

        amount = float(input("New Amount: "))

        category = input("New Category: ")

        date = input("New Date (YYYY-MM-DD): ")

        edit_expense(

            username,
            expense_id,
            name,
            amount,
            category,
            date
    )
            
    elif choice == "13":
        
        data = dashboard(expenses)
        
        print("\n====== FINANCE DASHBOARD =======\n")
        
        print(f"Total Expenses      : {data['total']}")
        
        print(f"Average Expense     : {round(data['average'], 2)}")
        
        print(f"Highest Expense     : {data['highest_name']} - {data['highest']}")
        
        print(f"Total Records       : {data['count']}")
        
        print(f"Top Category        : {data['top_category']}")
        
        print(f"Category Spending   : {data['top_amount']}")

    elif choice == "14":

        expense_graph(expenses)

    elif choice == "15":

        ai_insights(expenses)
        
    elif choice == "16":

        expenses = get_expenses(username)

        print("1. Highest")
        print("2. Lowest")
        print("3. Latest")

        sort_choice = input("Choose: ")

        if sort_choice == "1":

            data = sort_highest(expenses)

        elif sort_choice == "2":

            data = sort_lowest(expenses)

        else:

            data = sort_latest(expenses)

        show_expenses(data)
        
    elif choice == "17":

        category = input("Enter Category: ")

        data = filter_category(username, category)

        show_expenses(data)
        
    elif choice == "18":

        date = input("Enter Date (YYYY-MM-DD): ")

        data = search_by_date(username, date)

        show_expenses(data)
        
    elif choice == "19":

        stats = expense_statistics(expenses)

        print("\n====== STATISTICS DASHBOARD =======\n")

        print("Total Expenses :", stats["total"])
        
        print("Average Expense :", stats["average"])
        
        print("Highest Expense :", stats["highest"])
        
        print("Lowest Expense  :", stats["lowest"])
        
        print("Total Entries    :", stats["entries"])
        
    elif choice == "20":

        report = category_analytics(expenses)

        print("\n===== CATEGORY ANALYTICS =====")

        for category, percent in report.items():

            print(f"{category} : {percent}%")
            
    elif choice == "21":

        print("\n1. Highest Amount")

        print("2. Lowest Amount")

        print("3. Name A-Z")

        print("4. Latest Date")

        option = input("Choose sorting: ")

        if option == "1":

            expenses = sort_expenses(expenses, "highest")

        elif option == "2":

            expenses = sort_expenses(expenses, "lowest")

        elif option == "3":

            expenses = sort_expenses(expenses, "name")

        elif option == "4":

            expenses = sort_expenses(expenses, "latest")

        save_expenses(expenses, username)

        print("Expenses Sorted")

    elif choice == "22":

        break

    else:

        print(Fore.RED + "Invalid Choice")
        