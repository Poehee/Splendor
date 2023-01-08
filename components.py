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
    GOLD=6
    PINK=7
    WILD=GOLD
    RARE=PINK    

class Chips:
    def __init__(self) -> None:
        self.complete_set = []
        # Read about unpack with *: https://stackoverflow.com/questions/1720421/how-do-i-concatenate-two-lists-in-python
        # Many ways to join two lists: https://www.digitalocean.com/community/tutorials/concatenate-lists-python
        for color in Color:
            self.complete_set += [color.value] * config.chipcount.color

        self.complete_set += [SpecialChip.WILD.value] * config.chipcount.wilds
        self.complete_set += [SpecialChip.RARE.value] * config.chipcount.rares
        
        random.shuffle(self.complete_set)

class Bag:
    def __init__(self) -> None:
        self.chips = Chips().complete_set #When bag is instantiated, directly fill it with all the chips

#    def fill(self, chips: Chips):
#        self.chips = chips

    def draw_chip(self) -> int:
        if len(self.chips) == 0:
            return None
        return self.chips.pop(0)

class Board:
    # Using (in)comprehension: https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/
    squares = [[None for i in range(config.constants.board_size)] for j in range(config.constants.board_size)]
    def fill(self, bag: Bag) -> None:
        pass

if __name__ == "__main__":
    print(Color(3))                # Color.BLUE
    print(SpecialChip.GOLD.value)  # 6
    print(type (Color.RED))        # <enum 'Color'>
    print(SpecialChip.WILD)        # SpecialChip.GOLD
    print(Chips().complete_set)
    print(Board().squares)
    print(Chips())

    bag = Bag()
    print(bag.chips)

    for _ in range(len(bag.chips)):
        print(bag.draw_chip())

    print("Empty list....")  
    for _ in range(len(bag.chips)):
        print(bag.draw_chip())

    print("Now what, no more chips - what happens when we draw?")
    print(bag.draw_chip())
