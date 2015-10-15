#! /usr/bin/env python3

class Board:
    def __init__(self, M, N):
        self.board = []
        for row in range(M):
            temple = []
            for column in range(N):
                temple.append(False)

            self.board.append(temple)
            
                

