from dataclasses import dataclass
from enum import Enum, auto
from typing import Any
from settings import config
from math import floor, ceil

import copy
import random

class Clockwise(Enum):
    DOWN=auto()
    LEFT=auto()
    UP=auto()
    RIGHT=auto()

class Color(Enum):
    RED=1
    GREEN=2
    BLUE=3
    BLACK=4
    WHITE=5

class SpecialChip(Enum):
    GOLD=6 #Gold are wilds (substitute every other color or rare)
    PINK=7 #Pink are rares
    WILD=GOLD
    RARE=PINK    

class Chips:
    def __init__(self) -> None:
        self.full_set = []
        # Read about unpack with *: https://stackoverflow.com/questions/1720421/how-do-i-concatenate-two-lists-in-python
        # Many ways to join two lists: https://www.digitalocean.com/community/tutorials/concatenate-lists-python
        pass

    def get_full_set(self) -> list[int]:
        for color in Color:
            self.full_set += [color.value] * config.chipcount.color

        self.full_set += [SpecialChip.WILD.value] * config.chipcount.wilds
        self.full_set += [SpecialChip.RARE.value] * config.chipcount.rares

        return self.full_set

class Bag:
    def __init__(self) -> None:
        self.chips: list = []
        pass

    def fill_with_full_set(self):
        self.chips = Chips().get_full_set() #When bag is instantiated, directly fill it with all the chips
        random.shuffle(self.chips) #Chips are in a black, blind bag

    def draw_chip(self) -> int:
        if len(self.chips) == 0:
            return None
        return self.chips.pop(0)

class Board:
    def __init__(self) -> None:
        # Using (in)comprehension: https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/
        self.squares = [[None for i in range(config.constants.board_size)] for j in range(config.constants.board_size)]
        assert(len(self.squares[0])==len(self.squares[1])) #Board needs to be a square
        
        self.middle=[floor(len(self.squares[0])/2),floor(len(self.squares[1])/2)]
        self.flattened_board = self.rolled_inside_out()

    def rolled_inside_out(self) -> list:
        from itertools import cycle # https://stackoverflow.com/questions/36828526/moving-from-one-enum-state-to-the-next-and-cycling-through
        directions = cycle([Clockwise.DOWN, Clockwise.LEFT ,Clockwise.UP ,Clockwise.RIGHT])

        flat_board = [self.middle] # flat_board is needed for chip distribution, start in middle of the board, rounded down 

        def walk(direction: Clockwise):
            nonlocal flat_board
            x,y = flat_board[-1] # Start from last position
            if (direction == Clockwise.DOWN):
               y += 1 
            if (direction == Clockwise.LEFT):
               x -= 1       
            if (direction == Clockwise.UP):
               y -= 1       
            if (direction == Clockwise.RIGHT):
               x += 1

            assert x>=0, f"Expect x >= 0, got {x}" 
            assert y>=0, f"Expect y >= 0, got {y}"          
            flat_board += [[x,y]]

        # Walk inside out, clockwise, start direction is down. Startpoint is set to middle of the board.
        direction            = next(directions)
        nr_of_straight_steps = 1
        increase_nr_of_steps = False
        max_len_flat_board   = config.constants.board_size**2
        while True:
            if len(flat_board) >= max_len_flat_board:
                break
            for _ in range(nr_of_straight_steps):
                walk(direction)
            if increase_nr_of_steps:
                nr_of_straight_steps = min((nr_of_straight_steps+1), (max_len_flat_board - len(flat_board)))
            direction = next(directions)
            increase_nr_of_steps = not increase_nr_of_steps # Length increases after 2 turns, e.g. walk 2, turn, walk 2, turn, walk 3...  

        assert len(flat_board) == max_len_flat_board, f"Length of flat_board is {len(flat_board)}, this must be equal to {max_len_flat_board}"
        return flat_board

    def fill_from_bag(self, bag: Bag) -> None:
        # Iterate from middle, clockwise towards the outside - skipping already occupied squares
        # assume 0,0 (horizontal x,vertical y) as top left. Assuming a 5x5 grid.
        # start at [2,2], then [1,2] (go 1 left), then [1,1] (go 1 up) then 2 left [2,1], [3,1]
        # then 2 down [3,2], [3,3]. Then 3 left [2,3], [1,3], [0,3].
        # Then 3 up: [0,2], [0,1], [0,0] -- long sides left now: [1,0], [2,0], [3,0], [4,0]
        # Right side: [4,1], [4,2], [4,3], [4,4] en bottom last: [3,4], [2,4], [1,4], [0,4]. All done... 
#        print("self.flattened_board[0][0]", self.flattened_board[3][1])
        temp_flattened_board = copy.deepcopy(self.flattened_board)
        chip = bag.draw_chip()
        while (chip != None) and (len(temp_flattened_board) > 0):
            x,y = temp_flattened_board.pop(0)
            if self.squares[x][y] == None:
                self.squares[x][y] = chip
                chip = bag.draw_chip()

if __name__ == "__main__":
    print(Color(3))                # Color.BLUE
    print(SpecialChip.GOLD.value)  # 6
    print(type (Color.RED))        # <enum 'Color'>
    print(SpecialChip.WILD)        # SpecialChip.GOLD
    print(Chips().full_set)

    board = Board()
    print("Squares=" + str(board.squares))
    print("rolled_inside_out:" + str(board.flattened_board))
    
    bag = Bag()
    bag.fill_with_full_set()

    print("bag.chips=" + str(bag.chips))
    board.fill_from_bag(bag)

    print("bag.chips=" + str(bag.chips))
    assert(len(bag.chips)==0)

    print("Squares=" + str(board.squares))
    print("rolled_inside_out:" + str(board.flattened_board))
    assert(len(board.flattened_board)==config.constants.board_size**2) #no tampering with board.flattened_board
    