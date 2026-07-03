from collections import defaultdict


def expense_statistics(expenses):

    amounts = []

    for expense in expenses:

        parts = expense.strip().split("-")

        if len(parts) >= 4:

            try:

                amounts.append(float(parts[1]))

            except:

                pass

    if len(amounts) == 0:

        return {
            "total": 0,
            "highest": 0,
            "lowest": 0,
            "average": 0,
            "entries": 0
        }

    return {

        "total": sum(amounts),

        "highest": max(amounts),

        "lowest": min(amounts),

        "average": round(sum(amounts) / len(amounts), 2),

        "entries": len(amounts)
    }


def category_analytics(expenses):

    data = defaultdict(float)

    total = 0

    for expense in expenses:

        parts = expense.strip().split("-")

        if len(parts) >= 4:

            try:

                amount = float(parts[1])

                category = parts[2]

                data[category] += amount

                total += amount

            except:

                pass

    report = {}

    for category, amount in data.items():

        percent = (amount / total) * 100 if total > 0 else 0

        report[category] = round(percent, 2)

    return report


def sort_expenses(expenses, mode):

    clean = []

    for expense in expenses:

        parts = expense.strip().split("-")

        if len(parts) >= 4:

            clean.append(parts)

    if mode == "highest":

        clean.sort(key=lambda x: float(x[1]), reverse=True)

    elif mode == "lowest":

        clean.sort(key=lambda x: float(x[1]))

    elif mode == "name":

        clean.sort(key=lambda x: x[0].lower())

    elif mode == "latest":

        clean.sort(key=lambda x: x[3], reverse=True)

    result = []

    for item in clean:

        result.append("-".join(item))

    return result
