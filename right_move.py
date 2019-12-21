def display_board(lov):
  if not ((isinstance, list) and len(lov)) == 16:
    raise ValueError("invalid argument")

  output = ""
  output += "+-+-+-+-+\n"
  for row_index in range(4):
    row = lov[row_index * 4:row_index * 4 + 4]
    output += "|{0}|{1}|{2}|{3}| \n".format(*row)
    output += "+-+-+-+-+\n"

  return output

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
    #thisone
    elif lov[n] != lov[n - 1] and lov[n - 1] == lov[n - 2] and lov[n - 1] != lov[n - 3]:
        lov[n] = lov[n]
        lov[n - 1] = lov[n - 1] + lov[n - 2]
        lov[n - 2] = lov[n-3]
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

    #this one
    elif lov[n] != lov[n-1] and lov[n - 1] != lov[n - 2] and lov[n - 2] == lov[n - 3]:
        lov[n] = lov[n]
        lov[n - 1] = lov[n - 1]
        lov[n - 2] = lov[n - 2] + lov[n - 3]
        lov[n - 3] = "."
    #this one
    elif lov[n] == lov[n - 1] and lov[n] != lov[n - 2] and lov[n - 2] != lov[n - 3]:
        lov[n] = lov[n] +lov[n - 1]
        lov[n - 1] = lov[n - 2]
        lov[n - 2] = lov[n - 3]
        lov[n - 3] = "."
    #this one
    elif lov[n] != lov[n-2] and lov[n-1] == "." and lov[n-3] == ".":
        lov[n] = lov[n]
        lov[n - 1] = lov[n - 2]
        lov[n - 2] = "."
        lov[n - 3] = "."
    #this one
    elif lov[n] != lov[n-3] and lov[n-1] == "." and lov[n] == lov[n-2]:
        lov[n] = lov[n] + lov[n-2]
        lov[n - 1] = lov[n - 3]
        lov[n - 2] = "."
        lov[n - 3] = "."
    # this one
    elif lov[n] != lov[n - 1] and lov[n - 1] == lov[n - 3] and lov[n - 2] == ".":
        lov[n] = lov[n]
        lov[n - 1] = lov[n - 1] + lov[n - 3]
        lov[n - 2] = "."
        lov[n - 3] = "."
    #this one
    elif lov[n] != lov[n - 2] and lov[n - 2] == lov[n - 3] and lov[n - 1] == ".":
        lov[n] = lov[n]
        lov[n - 1] = lov[n - 2] + lov[n - 3]
        lov[n - 2] = "."
        lov[n - 3] = "."
    # this one
    elif lov[n] != lov[n - 2] and lov[n - 1] == "." and lov[n - 2] != lov[n-3]:
        lov[n] = lov[n]
        lov[n - 1] = lov[n - 2]
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
    move_to_the_right(lov, n=3)
    adding_and_conditions_to_the_right(lov, n=3)
    move_to_the_right(lov, n=7)
    adding_and_conditions_to_the_right(lov, n=7)
    move_to_the_right(lov, n=11)
    adding_and_conditions_to_the_right(lov, n=11)
    move_to_the_right(lov, n=15)
    adding_and_conditions_to_the_right(lov, n=15)
    return display_board(lov)
