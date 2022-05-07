import numpy as np
from torch import int64

class Game():
    def __init__(self) -> None:
        self.gamestep = 0
        self.grid_x=15
        self.grid_y=7
        self.board = [['1' for i in range(self.grid_x)] for i in range(self.grid_y)]
        self.player_1_funds = 5
        self.player_2_funds = 5

    def print_board(self) -> None:
        # First row
        print(f"  ", end='')
        game='~'
        c=65
        for j in range(self.grid_x):
            print(f"|{j+1:5} ", end='')
        print(f"| ", end='')
        print()
        print(f'{(self.grid_x*4+4)*"-"}')
        # Other rows
        for i in range(self.grid_y):
            print(f"{chr(c+i)} ", end='')
            for j in range(self.grid_x):
                print(f"| {self.board[i][j]:4} ", end='')
            print(f"| ", end='')
            print()
            print(f'{(self.grid_x*7+4)*"-"}')



class Piece():
    def __init__(self) -> None:
        self.char='A'
        self.side='w'
        pass
    def __print_character(self) ->str:
        return self.char+self.side

if __name__=='__main__':
    myGame = Game()
    myGame.print_board()