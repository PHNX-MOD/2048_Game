# 2048_Game

The 2048 game is a single player turn-based game against the computer.
The game process is about moving and assembling tiles across the game field.
The objective is to assemble a tile with the value of 2048.
The field is a square of 4x4 cells.
A cell may be empty or contain a tile.
Tiles contain a number which is a power of 2, starting with 2: 2, 4, 8, etc.
A turn in the game comprises the following steps.


First, the player presses a key corresponding to the sides of the field:
up, down, left or right. All the tiles on the board are moved to that side, such that
there would be no empty cells between that side's border and the closest tile.
If there are any adjacent tiles of the same value in the direction of the move,
they are combined into one tile with twice as great a value, starting from the closest
such tile to the border in which direction the move is made.
Example:
2  4  .  .                          .  .  2  4
4  4  8  .       moved right: --->  .  .  8  8
8  8  8  16                         .  8 16 16
.  8  8  32                         .  . 16 32


If there are no tiles to move or combine, the key press has no effect.


Otherwise, a tile is added to a randomly selected empty cell, with a randomly selected
value of either 2 or 4.


If after adding a tile there are no empty cells or no adjacent tiles of the same value
that could be combined, the game is over.


Otherwise, the player may make the next turn.



The game begins with three tiles with random values of either 2 or 4, in random cells.



