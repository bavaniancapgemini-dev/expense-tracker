def total_expense(expenses):

    total = 0

    for item in expenses:

        amount = int(item.split("-")[1])

        total += amount

    return total