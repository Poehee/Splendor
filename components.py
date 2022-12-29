from enum import Enum

class Color(Enum):
    GOLD=1
    PINK=2
    RED=3
    GREEN=4
    BLUE=5
    BLACK=6
    WHITE=7
    WILD=GOLD
    RARE=PINK    

class Scroll():
  def assign( self, )

if __name__ == "__main__":
    print( Color(3) )         #Color.RED
    print( Color.GOLD.value ) #1
    print( type (Color.RED) ) #<enum 'Color'>
    print( Color.WILD )       #GOLD
