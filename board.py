from settings import *

class Board():
    matrix = [[0 for i in range(config.constants.board_size)] for j in range(config.constants.board_size)]
    pass

if __name__ == "__main__":
    print("Board.matrix", Board.matrix)
    pass