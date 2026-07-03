def total_expense(expenses):

    total = 0

    for expense in expenses:

        parts = expense.split("-")

        amount = float(parts[1])

        total += amount

    return total


def highest_expense(expenses):

    highest_name = ""
    highest_amount = 0

    for expense in expenses:

        parts = expense.split("-")

        name = parts[0]

        amount = float(parts[1])

        if amount > highest_amount:

            highest_amount = amount

            highest_name = name

    return highest_name, highest_amount


def average_expense(expenses):

    if len(expenses) == 0:

        return 0

    total = total_expense(expenses)

    return total / len(expenses)


def category_report(expenses):

    report = {}

    for expense in expenses:

        parts = expense.split("-")

        category = parts[2]

        if category in report:

            report[category] += 1

        else:

            report[category] = 1

    return report

def monthly_report(expenses):

    report = {}

    for expense in expenses:

        parts = expense.split("-")

        # Skip broken data
        if len(parts) < 3:

            continue

        category = parts[2]

        amount = float(parts[1])

        if category in report:

            report[category] += amount

        else:

            report[category] = amount

    return report

def dashboard(expenses):

    total = 0

    highest = 0

    highest_name = ""

    categories = {}

    count = 0

    for expense in expenses:

        parts = expense.split("-")

        if len(parts) < 4:

            continue

        name = parts[0]

        amount = float(parts[1])

        category = parts[2]

        total += amount

        count += 1

        if amount > highest:

            highest = amount

            highest_name = name

        if category in categories:

            categories[category] += amount

        else:

            categories[category] = amount

    average = 0

    if count > 0:

        average = total / count

    top_category = "None"

    top_amount = 0

    for cat, amt in categories.items():

        if amt > top_amount:

            top_amount = amt

            top_category = cat

    return {

        "total": total,

        "average": average,

        "highest": highest,

        "highest_name": highest_name,

        "count": count,

        "top_category": top_category,

        "top_amount": top_amount

    }