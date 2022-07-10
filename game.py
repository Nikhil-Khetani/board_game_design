import numpy as np


class Game():
    def __init__(self) -> None:
        self.gamestep = 0
        self.grid_x=5
        self.grid_y=7
        self.board = [[EmptyPiece(i,j, self.grid_x, self.grid_y) for i in range(self.grid_x)] for j in range(self.grid_y)]
        self.player_1_funds = 5
        self.player_2_funds = 5

        self.game_queue = []

    def print_board(self) -> None:
        # First row
        print(f"  ", end='')
        char_startpoint=65
        for j in range(self.grid_x):
            print(f"|{j+1:5} ", end='')
        print(f"| ", end='')
        print()
        print(f'{(self.grid_x*4+4)*"-"}')
        # Other rows
        for i in range(self.grid_y):
            print(f"{chr(char_startpoint+i)} ", end='')
            for j in range(self.grid_x):
                print(f"| {self.board[i][j].print_character():4} ", end='')
            print(f"| ", end='')
            print()
            print(f'{(self.grid_x*7+4)*"-"}')




class Piece():
    def __init__(self,x,y,xmax,ymax) -> None:
        self.char='A'
        self.side='w'
        self.x=x
        self.y=y
        self.xmax = xmax
        self.ymax = ymax
        pass

    def print_character(self) -> str:
        return self.char+self.side

    def possible_moves(self)-> list:
        return []

class EmptyPiece(Piece):
    def __init__(self,x,y,xmax,ymax) -> None:
        super().__init__(x,y,xmax,ymax)
        self.side='~'
        self.char='~'

    def possible_moves(self)-> list:
        return []
        


if __name__=='__main__':
    myGame = Game()
    myGame.print_board()
    p = EmptyPiece(1,2,2,3)
    print(p.print_character())
    print(p.y)
