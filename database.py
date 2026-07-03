import sqlite3


conn = sqlite3.connect("expense_tracker.db")

cursor = conn.cursor()


# USERS TABLE

cursor.execute("""

CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT UNIQUE,

    password TEXT

)

""")


# EXPENSE TABLE

cursor.execute("""

CREATE TABLE IF NOT EXISTS expenses (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT,

    name TEXT,

    amount REAL,

    category TEXT,

    date TEXT

)

""")

conn.commit()


# =========================
# USER FUNCTIONS
# =========================

def register_user(username, password):

    try:

        cursor.execute(

            "INSERT INTO users (username, password) VALUES (?, ?)",

            (username, password)

        )

        conn.commit()

        return True

    except:

        return False


def login_user(username, password):

    cursor.execute(

        "SELECT * FROM users WHERE username=? AND password=?",

        (username, password)

    )

    return cursor.fetchone()


# =========================
# EXPENSE FUNCTIONS
# =========================

def add_expense(username, name, amount, category, date):

    cursor.execute(

        """

        INSERT INTO expenses

        (username, name, amount, category, date)

        VALUES (?, ?, ?, ?, ?)

        """,

        (username, name, amount, category, date)

    )

    conn.commit()


def get_expenses(username):

    cursor.execute(

        "SELECT name, amount, category, date FROM expenses WHERE username=?",

        (username,)

    )

    return cursor.fetchall()


def delete_expense(username, expense_id):

    cursor.execute(

        "DELETE FROM expenses WHERE id=? AND username=?",

        (expense_id, username)

    )

    conn.commit()