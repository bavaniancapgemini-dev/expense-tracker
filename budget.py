from report import total_expense


def remaining_budget(budget, expenses):

    total = total_expense(expenses)

    remaining = budget - total

    return remaining