from database import *

def filter_category(username, category):

    conn = sqlite3.connect("expense_tracker.db")

    cursor = conn.cursor()

    cursor.execute(

        """

        SELECT * FROM expenses

        WHERE username=? AND category=?

        """,

        (username, category)

    )

    data = cursor.fetchall()

    conn.close()

    return data


def search_by_date(username, date):

    conn = sqlite3.connect("expense_tracker.db")

    cursor = conn.cursor()

    cursor.execute(

        """

        SELECT * FROM expenses

        WHERE username=? AND date=?

        """,

        (username, date)

    )

    data = cursor.fetchall()

    conn.close()

    return data