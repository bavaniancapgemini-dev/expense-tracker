def show_expenses(expenses):

    print("\n---- EXPENSES ----")

    if len(expenses) == 0:

        print("No expenses found")

    else:

        for i, expense in enumerate(expenses):

            print(i + 1, "-", expense)