def sort_highest(expenses):

    return sorted(

        expenses,

        key=lambda x: x[1],

        reverse=True

    )


def sort_lowest(expenses):

    return sorted(

        expenses,

        key=lambda x: x[1]

    )


def sort_latest(expenses):

    return sorted(

        expenses,

        key=lambda x: x[3],

        reverse=True

    )