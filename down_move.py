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

def move_to_the_down(lov, n=None):
    if lov[n] == "." and lov[n - 4] == "." and lov[n - 8] == "." and lov[n - 12] == ".":
        pass

    elif lov[n] == ".":
        lov[n] = lov[n - 4]
        lov[n - 4] = lov[n - 8]
        lov[n - 8] = lov[n - 12]
        lov[n - 12] = '.'
        if lov[n] == ".":
            lov[n] = lov[n - 4]
            lov[n - 4] = lov[n - 8]
            lov[n - 8] = "."
            lov[n - 12] = '.'
            if lov[n] == ".":
                lov[n] = lov[n - 4]
                lov[n - 4] = "."
                lov[n - 8] = "."
                lov[n - 12] = '.'
        return display_board(lov)


def adding_and_conditions_to_the_down(lov, n=None):
    if lov[n] == "." and lov[n - 4] == "." and lov[n - 8] == "." and lov[n - 12] == ".":
        pass

    elif lov[n] == lov[n - 4] == lov[n - 8] == lov[n - 12]:
        lov[n] = lov[n] + lov[n - 4]
        lov[n - 4] = lov[n - 8] + lov[n - 12]
        lov[n - 8] = "."
        lov[n - 12] = "."


    elif lov[n] == lov[n - 4] and lov[n - 8] == "." and lov[n - 12] == ".":
        lov[n] = lov[n] + lov[n - 4]
        lov[n - 4] = "."
        lov[n - 8] = "."
        lov[n - 12] = "."


    elif lov[n] == lov[n - 4] and lov[n - 8] == lov[n - 12]:  # 2 cell value are equal
        lov[n] = lov[n - 4] + lov[n]
        lov[n - 4] = lov[n - 8] + lov[n - 12]
        lov[n - 8] = "."
        lov[n - 12] = "."
    
    #this one
    elif lov[n] != lov[n - 4] and lov[n - 4] == lov[n - 8] and lov[n - 4] != lov[n - 12]:
        lov[n] = lov[n]
        lov[n - 4] = lov[n - 4] + lov[n - 8]
        lov[n - 8] = lov[n - 12]
        lov[n - 12] = "."



    elif lov[n] == lov[n - 4] and lov[n] != lov[n - 8] and lov[n - 12] == ".":
        lov[n] = lov[n] + lov[n - 4]
        lov[n - 4] = lov[n - 8]
        lov[n - 8] = "."
        lov[n - 12] = "."


    elif lov[n] == lov[n - 8] and lov[n - 4] == "." and lov[n - 12] == ".":
        lov[n] = lov[n - 8] + lov[n]
        lov[n - 4] = "."
        lov[n - 8] = "."
        lov[n - 12] = "."

    elif lov[n] == lov[n - 12] and lov[n - 4] == "." and lov[n - 8] == ".":
        lov[n] = lov[n] + lov[n - 12]
        lov[n - 4] = "."
        lov[n - 8] = "."
        lov[n - 12] = "."

    elif lov[n] != lov[n - 4] and lov[n - 8] == "." and lov[n - 12] == ".":
        pass

    elif lov[n] == lov[n - 4] and lov[n] == lov[n - 8] and lov[n] != lov[n - 12]:
        lov[n] = lov[n - 4] + lov[n]
        lov[n - 4] = lov[n - 8]
        lov[n - 8] = lov[n - 12]
        lov[n - 12] = "."

    elif lov[n] != lov[n - 4] and lov[n - 4] == lov[n - 8] and lov[n - 4] == lov[n - 12]:
        lov[n] = lov[n]
        lov[n - 4] = lov[n - 4] + lov[n - 8]
        lov[n - 8] = lov[n - 12]
        lov[n - 12] = "."

        # this one
    elif lov[n] != lov[n - 4] and lov[n - 4] != lov[n - 8] and lov[n - 8] == lov[n - 12]:
        lov[n] = lov[n]
        lov[n - 4] = lov[n - 4]
        lov[n - 8] = lov[n - 8] + lov[n - 12]
        lov[n - 12] = "."
    # this one
    elif lov[n] == lov[n - 4] and lov[n] != lov[n - 8] and lov[n - 8] != lov[n - 12]:
        lov[n] = lov[n] + lov[n - 4]
        lov[n - 4] = lov[n - 8]
        lov[n - 8] = lov[n - 12]
        lov[n - 12] = "."
    # this one
    elif lov[n] != lov[n - 8] and lov[n - 4] == "." and lov[n - 12] == ".":
        lov[n] = lov[n]
        lov[n - 4] = lov[n - 8]
        lov[n - 8] = "."
        lov[n - 12] = "."
    #this one
    elif lov[n] != lov[n - 12] and lov[n - 4] == "." and lov[n] == lov[n - 8]:
        lov[n] = lov[n] + lov[n - 8]
        lov[n - 4] = lov[n - 12]
        lov[n - 8] = "."
        lov[n - 12] = "."
    #this one
    elif lov[n] != lov[n - 4] and lov[n - 4] == lov[n - 12] and lov[n - 8] == ".":
        lov[n] = lov[n]
        lov[n - 4] = lov[n - 4] + lov[n - 12]
        lov[n - 8] = "."
        lov[n - 12] = "."
    #this one
    elif lov[n] != lov[n - 8] and lov[n - 4] == "." and lov[n - 8] != lov[n - 12]:
        lov[n] = lov[n]
        lov[n - 4] = lov[n - 8]
        lov[n - 8] = lov[n - 12] 
        lov[n - 12] = "."
    
        
    elif lov[n] != lov[n - 8] and lov[n - 8] == lov[n - 12] and lov[n - 4] == ".":
        lov[n] = lov[n]
        lov[n - 4] = lov[n - 8] + lov[n - 12]
        lov[n - 8] = "."
        lov[n - 12] = "."


    elif lov[n - 4] == "." and lov[n - 12] == "." and lov[n] != lov[n - 8]:
        lov.insert(n - 4, lov.pop(n - 8))
        lov[n - 8] = "."
        lov[n - 12] = "."

    elif lov[n] != lov[n - 12] and lov[n - 4] and lov[n - 8] == ".":
        lov.insert(n - 4, lov.pop(n - 12))
        lov[n - 8] = "."
        lov[n - 12] = "."

    elif lov[n - 4] == lov[n - 8] and lov[n - 4] != [n] and lov[n - 12] == ".":
        lov[n - 4] = lov[n - 4] + lov[n - 8]
        lov[n - 8] = "."
        lov[n - 12] = "."
    return lov


def down_movement(lov):
    move_to_the_down(lov, n=12)
    adding_and_conditions_to_the_down(lov, n=12)
    move_to_the_down(lov, n=13)
    adding_and_conditions_to_the_down(lov, n=13)
    move_to_the_down(lov, n=14)
    adding_and_conditions_to_the_down(lov, n=14)
    move_to_the_down(lov, n=15)
    adding_and_conditions_to_the_down(lov, n=15)
    return display_board(lov)