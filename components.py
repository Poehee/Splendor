from enum import Enum
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
        # Read about *: https://stackoverflow.com/questions/1720421/how-do-i-concatenate-two-lists-in-python
        for color in Color:
            self.bag += [color.value for i in range(config.chipcount.per_color)]

    def x__str__(self):
        return str(self.bag)

    #bag = [chip 
    matrix = [[0 for i in range(config.constants.board_size)] for j in range(config.constants.board_size)]
    pass

if __name__ == "__main__":
    print(Color(3))         #Color.BLUE
    print(SpecialChip.GOLD.value) #1
    print(type (Color.RED)) #<enum 'Color'>
    print(SpecialChip.WILD)       #GOLD
    print(Chips().matrix)
    print(Chips())
