def show_expenses(expenses):

    if len(expenses) == 0:

        print("No Expenses Found")

        return

    print("\n===== ALL EXPENSES =====\n")

    count = 1

    for expense in expenses:

        parts = expense.split("-")

        if len(parts) < 4:

            continue

        name = parts[0]

        amount = parts[1]

        category = parts[2]

        date = parts[3]

        print(f"{count}. {name}")

        print(f"   Amount   : {amount}")

        print(f"   Category : {category}")

        print(f"   Date     : {date}")

        print()

        count += 1