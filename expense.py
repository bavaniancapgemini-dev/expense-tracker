def show_expenses(expenses):

    print("\n===== ALL EXPENSES =====\n")

    for i, expense in enumerate(expenses, start=1):

        print(f"{i}. {expense[0]}")

        print(f"   Amount   : {expense[1]}")

        print(f"   Category : {expense[2]}")

        print(f"   Date     : {expense[3]}")

        print()