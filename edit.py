from database import *

def edit_expense(username, expense_id, name, amount, category, date):

    conn = sqlite3.connect("expense_tracker.db")

    cursor = conn.cursor()

    cursor.execute(

        """

        UPDATE expenses

        SET name=?, amount=?, category=?, date=?

        WHERE id=? AND username=?

        """,

        (name, amount, category, date, expense_id, username)

    )

    conn.commit()

    conn.close()

    print("Expense Updated")