import numpy as np
from torch import int64

class Game():
    def __init__(self) -> None:
        self.gamestep = 0
        self.grid_x=15
        self.grid_y=7
        self.board = [[' ' for i in range(self.grid_x)] for i in range(self.grid_y)]

    def print_board(self) -> None:
        # First row
        print(f"  ", end='')
        game='~'
        c=65
        for j in range(self.grid_x):
            print(f"|{j+1:2} ", end='')
        print(f"| ", end='')
        print()
        print(f'{(self.grid_x*4+4)*"-"}')

        # Other rows
        for i in range(self.grid_y):
            print(f"{chr(c+i)} ", end='')
            for j in range(self.grid_x):
                print(f"| {self.board[i][j]} ", end='')
            print(f"| ", end='')
            print()
            print(f'{(self.grid_x*4+4)*"-"}')



class Piece():
    def __init__(self) -> None:
        pass

if __name__=='__main__':
    myGame = Game()
    myGame.print_board()
    