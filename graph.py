import matplotlib.pyplot as plt


def expense_graph(expenses):

    categories = {}
    
    for expense in expenses:

        parts = expense.split("-")

        if len(parts) < 4:
            continue

        category = parts[2]
        amount = float(parts[1])

        if category in categories:

            categories[category] += amount

        else:

            categories[category] = amount

    labels = list(categories.keys())

    values = list(categories.values())

    plt.figure(figsize=(8, 5))

    plt.bar(labels, values)

    plt.title("Expense By Category")

    plt.xlabel("Category")

    plt.ylabel("Amount")

    plt.show()