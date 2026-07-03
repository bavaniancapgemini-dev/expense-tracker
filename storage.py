def save_expenses(expenses, username):

    filename = username + "_expenses.txt"

    with open(filename, "w") as file:

        for expense in expenses:

            file.write(expense + "\n")

def load_expenses(username):

    filename = username + "_expenses.txt"

    try:

        with open(filename, "r") as file:

            return [line.strip() for line in file.readlines()]

    except:

        return []
    
    
def export_csv(expenses):

    file = open("expenses.csv", "w")

    file.write("Name,Amount,Category\n")

    for expense in expenses:

        parts = expense.split("-")

        # Skip broken entries
        if len(parts) < 3:

            continue

        name = parts[0]

        amount = parts[1]

        category = parts[2]

        file.write(f"{name},{amount},{category}\n")

    file.close()

    print("Expenses Exported To expenses.csv")