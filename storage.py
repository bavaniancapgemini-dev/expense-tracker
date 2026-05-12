def save_expenses(expenses):

    file = open("expenses.txt", "w")

    for expense in expenses:

        file.write(expense + "\n")

    file.close()

def load_expenses():

    try:

        file = open("expenses.txt", "r")

        expenses = file.read().splitlines()

        file.close()

        return expenses

    except:

        return []