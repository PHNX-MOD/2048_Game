from up_move import up_movement
from down_move import down_movement
from right_move import right_movement
from left_move import left_movement
import random
import numpy as np

game_is_still_on = True

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

def first_three_random_numbers(lov):
  indices = [i for i, x in enumerate(lov) if x == "."]
  rand3= random.sample(indices, 3)
  lov[rand3[0]]= random.choice([2,4])
  lov[rand3[1]]= random.choice([2,4])
  lov[rand3[2]]= random.choice([2,4])
  return display_board(lov)

def radom_number(lov):
  indices = [i for i, x in enumerate(lov) if x == "."]
  randcell=np.random.choice(indices)
  lov[randcell]=random.choice([2,4])
  return display_board(lov)

def check_for_empty_cell(lov):
  indices = [i for i, x in enumerate(lov) if x == "."]
  global game_is_still_on
  if indices==[]:
    print("Game is Ended")
    game_is_still_on = False
  else:
    game_is_still_on = True

def check_if_won(lov):
  indices = [i for i, x in enumerate(lov) if x == 2048]
  global game_is_still_on
  if indices==[]:
    game_is_still_on = True
    return "game is still on"
  else:
    game_is_still_on = False
    return "game finished"

def input_the_move(lov):
  input_the_movement= input("input the movement r = right, l = left, u = up, d=down \n")
  if input_the_movement == "r":
    right_movement(lov)
  elif input_the_movement == "l":
    left_movement(lov)
  elif input_the_movement == "u":
    up_movement(lov)
  elif input_the_movement == "d":
    down_movement(lov)
  return display_board(lov)

def main():
  lov=["."]*16
  print (first_three_random_numbers(lov))
  while True:
    print(input_the_move(lov))
    check_for_empty_cell(lov)
    if game_is_still_on is False:
      break
    print(check_if_won(lov))
    if game_is_still_on is False:
      break
    print(radom_number(lov))



main()