#! /usr/bin/env python3

import random
import copy

from EggBoard import Board
from SimulatedAnnealing import SimulatedAnnealing as SA
from SimulatedAnnealing2 import SimulatedAnnealing as SA2
from DrawEggBoard import DrawBoard

class Problem1:
    """ Class for problem 1 in assignment 4"""
    
    def __init__(self, M, N, K):
        self.board = Board(M, N, K)
        self.width = M
        self.height = N
        self.egg_rule = K
    
    def get_temperature(self, time):
        """Return temperature based on a given time"""
        cur_temp = (10**7)/float(time**2)
        if cur_temp < 0.1:
            return 0
        else:
            return cur_temp
    
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
        new_board = self.copy(board)
        for i in range(10):
            new_board = self.make_change(new_board)
        return new_board
        
    def get_variations(self, board):
        """Will return a list of n boards with different changes"""
        variations = []
        for i in range(1000):
            variation = self.make_change(self.copy(board))
            variation.get_points()
            variations.append(variation)
        
        variations.sort(key=lambda board: board.points)
        
        return variations
    
    def get_points(self, board):
        """Return how many rules are broken"""
        return board.get_points()
    
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
    
    def copy_board(self):
        """Will make a copy of the main board object"""
        return copy.deepcopy(self.board)
    
    def print_board(self, board):
        """A function to print the board to console"""
        for row in board.get_board():
            for item in row:
                if item:
                    print("1", end=" ")
                else:
                    print("0", end=" ")
            print()

   

if __name__ == "__main__":
    ## Puzzle variant 1
    p = Problem1(5,5,2)
    p.populate_board()
    p.print_board(p.board)
    print(p.get_points(p.board))
    
    db = DrawBoard(p.board)
    db.draw_board()
    db.draw_eggs()
    db.save("images/1-before%i.png" %(p.board.get_points()))
    
    s = SA2()
    sa_board = s.run(p.board, 0.02, p.get_variations, p.get_points)
    p.print_board(sa_board)
    print(p.get_points(sa_board))
    
    db = DrawBoard(sa_board)
    db.draw_board()
    db.draw_eggs()
    db.save("images/1-after%i.png" %(sa_board.get_points()))
    
    ## Puzzle variant 2
    p = Problem1(6,6,2)
    p.populate_board()
    p.print_board(p.board)
    print(p.get_points(p.board))
    
    db = DrawBoard(p.board)
    db.draw_board()
    db.draw_eggs()
    db.save("images/2-before%i.png" %(p.board.get_points()))
    
    s = SA2()
    sa_board = s.run(p.board, 0.02, p.get_variations, p.get_points)
    p.print_board(sa_board)
    print(p.get_points(sa_board))
    
    db = DrawBoard(sa_board)
    db.draw_board()
    db.draw_eggs()
    db.save("images/2-after%i.png" %(sa_board.get_points()))
    
    ## Puzzle variant 3
    p = Problem1(8,8,1)
    p.populate_board()
    p.print_board(p.board)
    print(p.get_points(p.board))
    
    db = DrawBoard(p.board)
    db.draw_board()
    db.draw_eggs()
    db.save("images/3-before%i.png" %(p.board.get_points()))
    
    s = SA2()
    sa_board = s.run(p.board, 0.02, p.get_variations, p.get_points)
    p.print_board(sa_board)
    print(p.get_points(sa_board))
    
    db = DrawBoard(sa_board)
    db.draw_board()
    db.draw_eggs()
    db.save("images/3-after%i.png" %(sa_board.get_points()))
    
    ## Puzzle variant 4
    p = Problem1(10,10,3)
    p.populate_board()
    p.print_board(p.board)
    print(p.get_points(p.board))
    
    db = DrawBoard(p.board)
    db.draw_board()
    db.draw_eggs()
    db.save("images/4-before%i.png" %(p.board.get_points()))
    
    s = SA2()
    sa_board = s.run(p.board, 0.02, p.get_variations, p.get_points)
    p.print_board(sa_board)
    print(p.get_points(sa_board))
    
    db = DrawBoard(sa_board)
    db.draw_board()
    db.draw_eggs()
    db.save("images/4-after%i.png" %(sa_board.get_points()))
