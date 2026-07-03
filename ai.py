def ai_insights(expenses):

    total = 0

    categories = {}

    count = 0

    for expense in expenses:

        parts = expense.split("-")

        if len(parts) < 4:
            continue

        amount = float(parts[1])

        category = parts[2]

        total += amount

        count += 1

        if category in categories:

            categories[category] += amount

        else:

            categories[category] = amount

    print("\n========== AI FINANCIAL INSIGHTS ==========\n")

    print(f"Total Spending: {total}")

    print(f"Total Transactions: {count}")

    if count > 0:

        average = total / count

        print(f"Average Expense: {round(average, 2)}")

    highest_category = ""

    highest_amount = 0

    for category, amount in categories.items():

        if amount > highest_amount:

            highest_amount = amount

            highest_category = category

    print(f"\nHighest Spending Category: {highest_category}")

    print(f"Amount Spent: {highest_amount}")

    # SMART INSIGHTS

    print("\n========== RECOMMENDATIONS ==========\n")

    if total > 10000:

        print("⚠ Your spending is very high")

    elif total > 5000:

        print("⚠ Moderate spending detected")

    else:

        print("✅ Spending level looks healthy")

    if highest_category.lower() == "food":

        print("🍔 Food expenses are high. Try reducing outside meals.")

    elif highest_category.lower() == "shopping":

        print("🛍 Shopping expenses are high. Avoid impulse purchases.")

    elif highest_category.lower() == "travel":

        print("✈ Travel spending is dominating your budget.")

    elif highest_category.lower() == "gaming":

        print("🎮 Gaming expenses are increasing rapidly.")

    else:

        print("✅ Category spending looks balanced")

    savings = total * 0.20

    print(f"\n💰 Suggested Monthly Savings: {round(savings, 2)}")

    # HEALTH SCORE

    if total < 3000:

        score = 95

    elif total < 7000:

        score = 75

    else:

        score = 50

    print(f"\n🏦 Financial Health Score: {score}/100")