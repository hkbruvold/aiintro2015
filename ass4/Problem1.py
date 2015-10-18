#! /usr/bin/env python3

import random
import copy

from EggBoard import Board
from SimulatedAnnealing import SimulatedAnnealing as SA

class Problem1:
    """ Class for problem 1 in assignment 4"""
    
    def __init__(self, M, N, K):
        self.board = Board(M, N)
        self.width = M
        self.height = N
        self.egg_rule = K
    
    def get_temperature(self, time):
        start_temp = 10000
        cur_temp = start_temp - time
        return max(cur_temp, 0)
    
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
        
        return board
    
    def get_variation(self, board):
        return self.make_change(self.copy(board))
        
    ## TODO: consider if necessary
    def get_variations(self, n):
        """Will return a list of n boards with different changes"""
        variations = []
        for i in range(n):
            variations.append(self.make_change(self.copy_board()))
        
        ## TODO: sort the list
        
        return variations
    
    def get_points(self, board):
        """Return how many rules are broken"""
        points = 0
        board = board.get_board()
        
        ## Check horizontally
        
        for row in board:
            eggs = row.count(True)
            if eggs > 2:
                points += (eggs - 2)
        
        ## Check vertically
        
        count = [0]*len(board[0])
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x]: count[x] += 1
        for eggs in count:
            if eggs > 2:
                points += (eggs - 2)
        
        ## Check diagonally topleft/bottomright
        
        count = [0]*(len(board)+len(board[0])-1) # create count list for diagonals
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x]: count[x-y] += 1 # shift count index by y
        for eggs in count:
            if eggs > 2:
                points += (eggs - 2)
        
        ## Check diagonally topright/bottomleft
        
        count = [0]*(len(board)+len(board[0])-1) # create count list for diagonals
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x]: count[x+y] += 1 # shift count index by y
        for eggs in count:
            if eggs > 2:
                points += (eggs - 2)
        
        return points
    
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
                
    def copy(self, obj):
        """Will make a "deep" copy of object"""
        return copy.deepcopy(obj)
    
    ## TODO: consider if necessary
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
    print(p.get_points(p.board))
    s = SA()
    sa_board = s.run(p.board, p.get_temperature, p.get_variation, p.get_points)
    p.print_board(sa_board)
    print(p.get_points(sa_board))
