def move_to_the_right(lov, n=None):
    if lov[n] == "." and lov[n - 1] == "." and lov[n - 2] == "." and lov[n - 3] == ".":
        pass

    elif lov[n] == ".":
        lov[n] = lov[n - 1]
        lov[n - 1] = lov[n - 2]
        lov[n - 2] = lov[n - 3]
        lov[n - 3] = '.'
        if lov[n] == ".":
            lov[n] = lov[n - 1]
            lov[n - 1] = lov[n - 2]
            lov[n - 2] = "."
            lov[n - 3] = '.'
            if lov[n] == ".":
                lov[n] = lov[n - 1]
                lov[n - 1] = "."
                lov[n - 2] = "."
                lov[n - 3] = '.'
        return display_board(lov)


def adding_and_conditions_to_the_right(lov, n=None):
    if lov[n] == "." and lov[n - 1] == "." and lov[n - 2] == "." and lov[n - 3] == ".":
        pass

    elif lov[n] == lov[n - 1] == lov[n - 2] == lov[n - 3]:
        lov[n] = lov[n] + lov[n - 1]
        lov[n - 1] = lov[n - 2] + lov[n - 3]
        lov[n - 2] = "."
        lov[n - 3] = "."


    elif lov[n] == lov[n - 1] and lov[n - 2] == "." and lov[n - 3] == ".":
        lov[n] = lov[n] + lov[n - 1]
        lov[n - 1] = "."
        lov[n - 2] = "."
        lov[n - 3] = "."


    elif lov[n] == lov[n - 1] and lov[n - 2] == lov[n - 3]:  # 2 cell value are equal
        lov[n] = lov[n - 1] + lov[n]
        lov[n - 1] = lov[n - 2] + lov[n - 3]
        lov[n - 2] = "."
        lov[n - 3] = "."


    elif lov[n] == lov[n - 1] and lov[n] != lov[n - 2] and lov[n - 3] == ".":
        lov[n] = lov[n] + lov[n - 1]
        lov.insert(n - 1, lov.pop(n - 2))
        lov[n - 2] = "."
        lov[n - 3] = "."


    elif lov[n] == lov[n - 2] and lov[n - 1] == "." and lov[n - 3] == ".":
        lov[n] = lov[n - 2] + lov[n]
        lov[n - 1] = "."
        lov[n - 2] = "."
        lov[n - 3] = "."

    elif lov[n] == lov[n - 3] and lov[n - 1] == "." and lov[n - 2] == ".":
        lov[n] = lov[n] + lov[n - 3]
        lov[n - 1] = "."
        lov[n - 2] = "."
        lov[n - 3] = "."

    elif lov[n] != lov[n - 1] and lov[n - 2] == "." and lov[n - 3] == ".":
        pass


    elif lov[n] != lov[n - 3] and lov[n] == lov[n - 1] and lov[n] == lov[n - 2]:
        lov[n] = lov[n - 1] + lov[n]
        lov[n - 1] = lov[n - 2]
        lov[n - 2] = lov[n - 3]
        lov[n - 3] = "."

    elif lov[n] != lov[n - 1] and lov[n - 1] == lov[n - 2] and lov[n - 1] == lov[n - 3]:
        lov[n] = lov[n]
        lov[n - 1] = lov[n - 1] + lov[n - 2]
        lov[n - 2] = lov[n - 3]
        lov[n - 3] = "."

    elif lov[n - 1] == "." and lov[n - 3] == "." and lov[n] != lov[n - 2]:
        lov.insert(n - 1, lov.pop(n - 2))
        lov[n - 2] = "."
        lov[n - 3] = "."

    elif lov[n] != lov[n - 3] and lov[n - 1] and lov[n - 2] == ".":
        lov.insert(n - 1, lov.pop(n - 3))
        lov[n - 2] = "."
        lov[n - 3] = "."

    elif lov[n - 1] == lov[n - 2] and lov[n - 1] != [n] and lov[n - 3] == ".":
        lov[n - 1] = lov[n - 1] + lov[n - 2]
        lov[n - 2] = "."
        lov[n - 3] = "."
    return lov


def right_movement(lov):
    move_to_the_right(lov, n=0)
    adding_and_conditions_to_the_right(lov, n=0)
    move_to_the_right(lov, n=4)
    adding_and_conditions_to_the_right(lov, n=4)
    move_to_the_right(lov, n=8)
    adding_and_conditions_to_the_right(lov, n=8)
    move_to_the_right(lov, n=12)
    adding_and_conditions_to_the_right(lov, n=12)
    return display_board(lov)