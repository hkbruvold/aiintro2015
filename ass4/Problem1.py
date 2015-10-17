#! /usr/bin/env python3

import random
import copy

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
    
    def make_change(self, board):
        """Will make one change to a random egg on the board"""
        egg = self.get_random_egg(board)
        
        x = random.randint(0, self.width-1)
        y = random.randint(0, self.height-1)
        while board.is_egg_at(x, y) == True:
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
        
        board.move_egg(egg[0], egg[1], x, y)
        
    
    def get_variations(self, n):
        """Will return a list of n boards with different changes"""
        variations = []
        for i in range(n):
            variations.append(self.make_change(self.copy_board()))
        
        ## TODO: sort the list
        
        return variations
    
    def get_points(self, board):
        """Return how many rules are broken"""
        pass
    
    def get_random_egg(self, board):
        """Return coordinate for a random egg on the board"""
        number_of_eggs = self.egg_rule * self.width
        egg = random.randint(0, number_of_eggs - 1)
        egg_counter = 0
        
        boardlist = board.get_board()
        for y in range(len(boardlist)):
            for x in range(len(boardlist[y])):
                if boardlist[y][x]:
                    if egg_counter == egg:
                        return (x, y)
                    egg_counter += 1
        raise Exception("egg_counter error, this should not happen")
                
    
    def copy_board(self):
        """Will make a copy of the main board object"""
        return copy.deepcopy(self.board)
    
    def print_board(self, board):
        for row in board.get_board():
            for item in row:
                if item:
                    print("1", end=" ")
                else:
                    print("0", end=" ")
            print()

    

if __name__ == "__main__":
    p = Problem1(5,5,2)
    p.populate_board()
    p.print_board(p.board)
    print()
    a = p.copy_board()
    p.make_change(a)
    p.print_board(a)
