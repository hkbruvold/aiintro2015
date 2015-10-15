#! /usr/bin/env python3

import random

from EggBoard import Board

class Problem1:
    """ Class for problem 1 in assignment 4"""
    
    def __init__(self, M, N, K):
        self.board = Board(M, N)
        self.width = M
        self.height = N
        self.egg_rule = K
    
    def populate_board(self):
        """fill the board with as many eggs as possible in random positions"""
        for row in self.board.get_board():
            row[random.randint(0, self.width-1)] = True
            for i in range(self.egg_rule-1):
                is_added = False
                while not is_added:
                    nextpos = random.randint(0, self.width-1)
                    if row[nextpos] == False:
                        row[nextpos] = True
                        is_added = True
                
    

if __name__ == "__main__":
    p = Problem1(5,5,2)
    p.populate_board()
