import os


USER_FILE = "users.txt"


def register(username, password):

    if not os.path.exists(USER_FILE):

        open(USER_FILE, "w").close()

    with open(USER_FILE, "r") as file:

        users = file.readlines()

    for user in users:

        parts = user.strip().split("-")

        if parts[0] == username:

            return False

    with open(USER_FILE, "a") as file:

        file.write(username + "-" + password + "\n")

    return True


def login(username, password):

    if not os.path.exists(USER_FILE):

        return False

    with open(USER_FILE, "r") as file:

        users = file.readlines()

    for user in users:

        parts = user.strip().split("-")

        if len(parts) < 2:

            continue

        if parts[0] == username and parts[1] == password:

            return True

    return False
