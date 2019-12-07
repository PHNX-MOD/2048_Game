import random
import numpy as np
def display_board(l1):
  if not ((isinstance, list) and len(l1)) == 16:
    raise ValueError("invalid argument")

  output = ""
  output += "+-+-+-+-+\n"
  for row_index in range(4):
    row = l1[row_index * 4:row_index * 4 + 4]
    output += "|{0}|{1}|{2}|{3}| \n".format(*row)
    output += "+-+-+-+-+\n"

  return output

def random_number():
  num = [2,4]
  return random.choice(num)

def random_cell():
  cell=[x for x in range(1,11)]
  return random.choice(cell)


def input_random_cell_value(lov):
  lov[random_cell()]=random_number()
  return display_board(lov)

def first_three_random_numbers(lov):
  rand3=np.random.randint(1,17,3)
  rand_cell1=rand3[0]
  rand_cell2=rand3[1]
  rand_cell3=rand3[2]
  lov[rand_cell1]=random.choice([2,4])
  lov[rand_cell2]=random.choice([2,4])
  lov[rand_cell3]=random.choice([2,4])
  return display_board(lov)

lov=["."]*16

def input_the_movement():
    input_the_move=input("Enter the movement !  \n")
    if input_the_move == 1:
        right_movement(lov)
        return display_board()
    elif input_the_move == 2:
        left_movement(lov)
    return display_board(lov)


def move_to_the_right(lov,n=None):
    if lov[n] == ".":
        lov.insert(n, lov.pop(n-1))
        lov.insert(n-1, lov.pop(n-2))
        lov.insert(n-2, lov.pop(n-3))
        if lov[n] == ".":
            lov.insert(n, lov.pop(n-1))
            lov.insert(n-1, lov.pop(n-2))
            lov[n-3] = "."
            lov[n-2] = "."
            if lov[n] == ".":
                lov.insert(n, lov.pop(n-1))
                lov[n-3] = "."
                lov[n-2] = "."
                lov[n-1] = "."


def adding_and_conditions_to_the_right(lov,n=None):
    #if lov[0:4] or lov[4:8] or lov[8:12] or lov[12:16] =="."*4:


    if lov[n] == lov[n-1] == lov[n-2] == lov[n-3]:
        lov[n-1] = lov[n-2]+lov[n-3]
        lov[n-2] = "."
        lov[n-3] = "."


    elif lov[n] == lov[n-1] and lov[n-2] == lov[n-3]:  # 2 cell value are equal
        lov[n] = lov[n-1] + lov[n]
        lov[n-1] = lov[n-2] + lov[n-3]
        lov[n-2] = "."
        lov[n-3] = "."

    elif lov[n] == lov[n-1] and lov[n] != lov[n-2] and lov[n-3]==".":
        lov[n]=lov[n]+lov[n-1]
        lov.insert(n - 1, lov.pop(n - 2))
        lov[n-2]="."
        lov[n-3]="."

    elif lov[n] == lov[n-2] and lov[n]==lov[n-1]: #3 cell value are equal
        lov[n]=lov[n-1]+lov[n]
        lov.insert(n-1, lov.pop(n-2))
        lov[n-2]="."
        lov[n-3]="."

    elif lov[n]==lov[n-1]:
        lov[n]=lov[n]+lov[n-1]
        lov.insert(n-1, lov.pop(n-2))
        lov.insert(n-2, lov.pop(n-3))
        lov[n-3]="."

    elif lov[n]==lov[n-2]:
        lov[n]=lov[n]+lov[n-2]
        lov[n-2]="."

    elif lov[n]==lov[n-3]:
        lov[n]=lov[n]+lov[n-3]
        lov[n-3]="."


    elif lov[n]==lov[n-3]:
        lov[n]=lov[n]+lov[n-3]
        lov[n-3]="."

    elif lov[n-1]=="." and lov[n-3] == "." and lov[n] != lov[n-2]:
        lov.insert(n-1, lov.pop(n-2))
        lov[n - 2] = "."
        lov[n - 3] = "."

    elif lov[n] != lov[n-3] and lov[n-1] and lov[n-2] == ".":
        lov.insert(n-1, lov.pop(n-3))
        lov[n-2] = "."
        lov[n-3] = "."

    elif lov[n-1] == lov[n-2] and lov[n-1] != [n] and lov[n-3]==".":
        lov[n-1] = lov[n-1] + lov[n-2]
        lov[n-2] = "."
        lov[n-3] = "."


    return display_board(lov)


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

def move_to_the_left(lov,n=None):
    if lov[n] == ".":
        lov.insert(n, lov.pop(n+1))
        lov.insert(n+1, lov.pop(n+2))
        lov.insert(n+2, lov.pop(n+3))
        if lov[n] == ".":
            lov.insert(n, lov.pop(n+1))
            lov.insert(n+1, lov.pop(n+2))
            lov[n+3] = "."
            lov[n+2] = "."
            if lov[n] == ".":
                lov.insert(n, lov.pop(n+1))
                lov[n+3] = "."
                lov[n+2] = "."
                lov[n+1] = "."


def adding_and_conditions_to_the_left(lov,n=None):
    #if lov[0:4] or lov[4:8] or lov[8:12] or lov[12:16] =="."*4:



    if lov[n] == lov[n+1] == lov[n+2] == lov[n+3]:
        lov[n+1] = lov[n+2]+lov[n+3]
        lov[n+2] = "."
        lov[n+3] = "."


    elif lov[n] == lov[n+1] and lov[n+2] == lov[n+3]:  # 2 cell value are equal
        lov[n] = lov[n+1] + lov[n]
        lov[n+1] = lov[n+2] + lov[n+3]
        lov[n+2] = "."
        lov[n+3] = "."

    elif lov[n] == lov[n+1] and lov[n] != lov[n+2] and lov[n+3]==".":
        lov[n]=lov[n]+lov[n+1]
        lov.insert(n+1, lov.pop(n+2))
        lov[n+2]="."
        lov[n+3]="."

    elif lov[n] == lov[n+2] and lov[n]==lov[n+1]: #3 cell value are equal
        lov[n]=lov[n+1]+lov[n]
        lov.insert(n+1, lov.pop(n+2))
        lov[n+2]="."
        lov[n+3]="."

    elif lov[n]==lov[n+1]:
        lov[n]=lov[n]+lov[n+1]
        lov.insert(n+1, lov.pop(n+2))
        lov.insert(n+2, lov.pop(n+3))
        lov[n+3]="."
        move_to_the_left()

    elif lov[n]==lov[n+2]:
        lov[n]=lov[n]+lov[n+2]
        lov[n+2]="."
        move_to_the_left()

    elif lov[n]==lov[n+3]:
        lov[n]=lov[n]+lov[n+3]
        lov[n+3]="."
        move_to_the_left()

    elif lov[n]==lov[n+3]:
        lov[n]=lov[n]+lov[n+3]
        lov[n+3]="."
        move_to_the_left()

    elif lov[n+1]=="." and lov[n+3] == "." and lov[n] != lov[n+2]:
        lov.insert(n+1, lov.pop(n+2))
        lov[n+2] = "."
        lov[n+3] = "."

    elif lov[n] != lov[n+3] and lov[n+1] and lov[n+2] == ".":
        lov.insert(n+1, lov.pop(n+3))
        lov[n+2] = "."
        lov[n+3] = "."

    elif lov[n+1] == lov[n+2] and lov[n+1] != [n] and lov[n+3]==".":
        lov[n+1] = lov[n+1] + lov[n+2]
        lov[n+2] = "."
        lov[n+3] = "."
    return lov

def left_movement(lov):
    move_to_the_left(lov, n=0)
    adding_and_conditions_to_the_left(lov, n=0)
    move_to_the_left(lov, n=4)
    adding_and_conditions_to_the_left(lov, n=4)
    move_to_the_left(lov, n=8)
    adding_and_conditions_to_the_left(lov, n=8)
    move_to_the_left(lov, n=12)
    adding_and_conditions_to_the_left(lov, n=12)
    return lov

def main():
    lov = ["."] * 16
    print ("Please enter 1 for right, 2 for left, 3 for up and 4 for down movements")
    print (first_three_random_numbers(lov))
    while True:
        input_the_movement()
        input_random_cell_value(lov)
        return display_board(lov)


print(main())

