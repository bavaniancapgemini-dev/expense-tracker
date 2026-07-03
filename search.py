def search_expense(keyword):

    with open("expenses.txt", "r") as file:

        for line in file:

            if keyword.lower() in line.lower():

                print(line)