from dataclasses import dataclass
from enum import Enum
from typing import Any
from settings import config

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
    bag=[]

    def __init__(self) -> None:
        # Read about unpack with *: https://stackoverflow.com/questions/1720421/how-do-i-concatenate-two-lists-in-python
        # Many ways to join two lists: https://www.digitalocean.com/community/tutorials/concatenate-lists-python
        for color in Color:
            self.bag += [color.value] * config.chipcount.color

        self.bag += [SpecialChip.WILD.value] * config.chipcount.wilds
        self.bag += [SpecialChip.RARE.value] * config.chipcount.rares

class Board:
    squares = [[None for i in range(config.constants.board_size)] for j in range(config.constants.board_size)]

class Bag:
    pass

if __name__ == "__main__":
    print(Color(3))                # Color.BLUE
    print(SpecialChip.GOLD.value)  # 6
    print(type (Color.RED))        # <enum 'Color'>
    print(SpecialChip.WILD)        # SpecialChip.GOLD
    print(Chips().bag)
    print(Board().squares)
    print(Chips())
