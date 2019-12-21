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

def move_to_the_up(lov, n=None):
    if lov[n] == "." and lov[n + 4] == "." and lov[n + 8] == "." and lov[n + 12] == ".":
        pass

    elif lov[n] == ".":
        lov[n] = lov[n + 4]
        lov[n + 4] = lov[n + 8]
        lov[n + 8] = lov[n + 12]
        lov[n + 12] = '.'
        if lov[n] == ".":
            lov[n] = lov[n + 4]
            lov[n + 4] = lov[n + 8]
            lov[n + 8] = "."
            lov[n + 12] = '.'
            if lov[n] == ".":
                lov[n] = lov[n + 4]
                lov[n + 4] = "."
                lov[n + 8] = "."
                lov[n + 12] = '.'
        return lov


def adding_and_conditions_to_the_up(lov, n=None):
    if lov[n] == "." and lov[n + 4] == "." and lov[n + 8] == "." and lov[n + 12] == ".":
        pass

    elif lov[n] == lov[n + 4] == lov[n + 8] == lov[n + 12]:
        lov[n] = lov[n] + lov[n + 4]
        lov[n + 4] = lov[n + 8] + lov[n + 12]
        lov[n + 8] = "."
        lov[n + 12] = "."


    elif lov[n] == lov[n + 4] and lov[n + 8] == "." and lov[n + 12] == ".":
        lov[n] = lov[n] + lov[n + 4]
        lov[n + 4] = "."
        lov[n + 8] = "."
        lov[n + 12] = "."


    elif lov[n] == lov[n + 4] and lov[n + 8] == lov[n + 12]:  # 2 cell value are equal
        lov[n] = lov[n + 4] + lov[n]
        lov[n + 4] = lov[n + 8] + lov[n + 12]
        lov[n + 8] = "."
        lov[n + 12] = "."
        
    #this one
    elif lov[n] != lov[n + 4] and lov[n + 4] == lov[n + 8] and lov[n + 4] != lov[n + 12]:
        lov[n] = lov[n]
        lov[n + 4] = lov[n + 4] + lov[n + 8]
        lov[n + 8] = lov[n + 12]
        lov[n + 12] = "."
    
    
    elif lov[n] == lov[n + 4] and lov[n] != lov[n + 8] and lov[n + 12] == ".":
        lov[n] = lov[n] + lov[n + 4]
        lov[n + 4] = lov[n + 8]
        lov[n + 8] = "."
        lov[n + 12] = "."


    elif lov[n] == lov[n + 8] and lov[n + 4] == "." and lov[n + 12] == ".":
        lov[n] = lov[n + 8] + lov[n]
        lov[n + 4] = "."
        lov[n + 8] = "."
        lov[n + 12] = "."

    elif lov[n] == lov[n + 12] and lov[n + 4] == "." and lov[n + 8] == ".":
        lov[n] = lov[n] + lov[n + 12]
        lov[n + 4] = "."
        lov[n + 8] = "."
        lov[n + 12] = "."

    elif lov[n] != lov[n + 4] and lov[n + 8] == "." and lov[n + 12] == ".":
        pass

    elif lov[n] == lov[n + 4] and lov[n] == lov[n + 8] and lov[n] != lov[n + 12]:
        lov[n] = lov[n + 4] + lov[n]
        lov[n + 4] = lov[n + 8]
        lov[n + 8] = lov[n + 12]
        lov[n + 12] = "."

    elif lov[n] != lov[n + 4] and lov[n + 4] == lov[n + 8] and lov[n + 4] == lov[n + 12]:
        lov[n] = lov[n]
        lov[n + 4] = lov[n + 4] + lov[n + 8]
        lov[n + 8] = lov[n + 12]
        lov[n + 12] = "."

     #this one
    elif lov[n] != lov[n + 4] and lov[n + 4] != lov[n + 8] and lov[n + 8] == lov[n + 12]:
        lov[n] = lov[n]
        lov[n + 4] = lov[n + 4]
        lov[n + 8] = lov[n + 8] + lov[n + 12]
        lov[n + 12] = "."
    
    # this one
    elif lov[n] == lov[n + 4] and lov[n] != lov[n + 8] and lov[n + 8] != lov[n + 12]:
        lov[n] = lov[n] + lov[n + 4]
        lov[n + 4] = lov[n + 8]
        lov[n + 8] = lov[n + 12]
        lov[n + 12] = "."
    # this one
    elif lov[n] != lov[n + 8] and lov[n + 4] == "." and lov[n + 12] == ".":
        lov[n] = lov[n]
        lov[n + 4] = lov[n + 8]
        lov[n + 8] = "."
        lov[n + 12] = "."
        
    # this one
    elif lov[n] != lov[n + 12] and lov[n + 4] == "." and lov[n] == lov[n + 8]:
        lov[n] = lov[n] + lov[n + 8]
        lov[n + 4] = lov[n + 12]
        lov[n + 8] = "."
        lov[n + 12] = "."
    # this one
    elif lov[n] != lov[n + 4] and lov[n + 4] == lov[n + 12] and lov[n + 8] == ".":
        lov[n] = lov[n]
        lov[n + 4] = lov[n + 4] + lov[n + 12]
        lov[n + 8] = "."
        lov[n + 12] = "."
    #this one
    elif lov[n] != lov[n + 8] and lov[n + 8] == lov[n + 12] and lov[n + 4] == ".":
        lov[n] = lov[n]
        lov[n + 4] = lov[n + 8] + lov[n + 12]
        lov[n + 8] = "."
        lov[n + 12] = "."
        # this one
    elif lov[n] != lov[n + 8] and lov[n + 4] == "." and lov[n + 8] != lov[n + 12]:
        lov[n] = lov[n]
        lov[n + 4] = lov[n + 8]
        lov[n + 8] = lov[n + 12]
        lov[n + 12] = "."


    elif lov[n + 4] == "." and lov[n + 12] == "." and lov[n] != lov[n + 8]:
        lov.insert(n + 4, lov.pop(n + 8))
        lov[n + 8] = "."
        lov[n + 12] = "."

    elif lov[n] != lov[n + 12] and lov[n + 4] and lov[n + 8] == ".":
        lov.insert(n + 4, lov.pop(n + 12))
        lov[n + 8] = "."
        lov[n + 12] = "."

    elif lov[n + 4] == lov[n + 8] and lov[n + 4] != [n] and lov[n + 12] == ".":
        lov[n + 4] = lov[n + 4] + lov[n + 8]
        lov[n + 8] = "."
        lov[n + 12] = "."
    return lov


def up_movement(lov):
    move_to_the_up(lov, n=0)
    adding_and_conditions_to_the_up(lov, n=0)
    move_to_the_up(lov, n=1)
    adding_and_conditions_to_the_up(lov, n=1)
    move_to_the_up(lov, n=2)
    adding_and_conditions_to_the_up(lov, n=2)
    move_to_the_up(lov, n=3)
    adding_and_conditions_to_the_up(lov, n=3)
    return display_board(lov)
