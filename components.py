from dataclasses import dataclass
from enum import Enum
from typing import Any
from settings import config
import random

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

    def get_full_set(self) -> []:
        for color in Color:
            self.full_set += [color.value] * config.chipcount.color

        self.full_set += [SpecialChip.WILD.value] * config.chipcount.wilds
        self.full_set += [SpecialChip.RARE.value] * config.chipcount.rares

        return self.full_set

class Bag:
    def __init__(self) -> None:
        self.chips = Chips().get_full_set() #When bag is instantiated, directly fill it with all the chips
        #self.chips = random.shuffle(Chips().full_set) #When bag is instantiated, directly fill it with all the chips
        random.shuffle(self.chips) #Chips are in a black, blind bag

    def draw_chip(self) -> int:
        if len(self.chips) == 0:
            return None
        return self.chips.pop(0)

class Board:
    # Using (in)comprehension: https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/
    squares = [[None for i in range(config.constants.board_size)] for j in range(config.constants.board_size)]
    def fill(self, bag: Bag) -> None:
        # Iterate from middle, clockwise towards the outside - skipping already occupied squares
        # assume 0,0 (horizontal x,vertical y) as top left. Assuming a 5x5 grid.
        # start at [2,2], then [1,2] (go 1 left), then [1,1] (go 1 up) then 2 left [2,1], [3,1]
        # then 2 down [3,2], [3,3]. Then 3 left [2,3], [1,3], [0,3].
        # Then 3 up: [0,2], [0,1], [0,0] -- long sides left now: [1,0], [2,0], [3,0], [4,0]
        # Right side: [4,1], [4,2], [4,3], [4,4] en bottom last: [3,4], [2,4], [1,4], [0,4]. All done... 
        pass

if __name__ == "__main__":
    print(Color(3))                # Color.BLUE
    print(SpecialChip.GOLD.value)  # 6
    print(type (Color.RED))        # <enum 'Color'>
    print(SpecialChip.WILD)        # SpecialChip.GOLD
    print(Chips().full_set)
    print(Board().squares)
    print(Chips())

    bag = Bag()
    print(bag.chips)

    for _ in range(len(bag.chips)):
        print(bag.draw_chip())

    print("Empty list....")  
    for _ in range(len(bag.chips)):
        print(bag.draw_chip())

    print("Now what, no more chips - what happens when we draw? We get...(expect None):")
    print(bag.draw_chip())
