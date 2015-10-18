#! /usr/bin/env python3

class Board:
    def __init__(self, M, N, K):
        self.board = []
        self.egg_rule = K
        self.points = 0
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
        
    def get_points(self):
        """Return how many rules are broken"""
        points = 0
        
        ## Check horizontally
        
        for row in self.board:
            eggs = row.count(True)
            if eggs > self.egg_rule:
                points += (eggs - self.egg_rule)
        
        ## Check vertically
        
        count = [0]*len(self.board[0])
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x]: count[x] += 1
        for eggs in count:
            if eggs > self.egg_rule:
                points += (eggs - self.egg_rule)
        
        ## Check diagonally topleft/bottomright
        
        count = [0]*(len(self.board)+len(self.board[0])-1) # create count list for diagonals
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x]: count[x-y] += 1 # shift count index by y
        for eggs in count:
            if eggs > self.egg_rule:
                points += (eggs - self.egg_rule)
        
        ## Check diagonally topright/bottomleft
        
        count = [0]*(len(self.board)+len(self.board[0])-1) # create count list for diagonals
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x]: count[x+y] += 1 # shift count index by y
        for eggs in count:
            if eggs > self.egg_rule:
                points += (eggs - self.egg_rule)
        
        self.points = points
        return points
