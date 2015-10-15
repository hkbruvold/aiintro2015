#! /usr/bin/env python3

class Board:
    def __init__(self, M, N):
        self.board = []
        for row in range(M):
            temple = []
            for column in range(N):
                temple.append(False)

            self.board.append(temple)


    def add_egg(self, x, y):
        self.board[y][x] = True

    def remove_egg(self, x, y):
        self.board[y][x] = False

    def move_egg(self, x, y, x2, y2):
        self.add_egg(x2,y2)
        self.remove_egg(x,y)

    def get_board(self):
        return self.board

    def is_egg_at(self, x, y):
        return self.board[y][x]
        
            
                

