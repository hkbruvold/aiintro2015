#! /usr/bin/env python3


from math import exp
from random import random, choice

class SimulatedAnnealing:
    """Implementiation of the general algorithm"""
    
    def run(self, start_board, dT, variations, points):
        """
        Runs the simmulated annealing algorithm. 
        Will run till temperature is 0 or a perfect solution is obtained
           
        Arguments:
        start_board: The initial board object
        dT: Temperature decreasing value
        variations: A function that returns a list of neighbouring boards
        points: A function to calculate (negative) points for a board"""
        
        temperature = 10
        current = start_board
        current_points = points(start_board)
        while True:
            if temperature < 0.1 or current_points < 1:
                return current
            nextlist = variations(current)
            best_board = nextlist[0]
            q = (current_points - points(best_board)) / current_points
            p = min(1, exp(-q/temperature))
            if random() > p:
                current = best_board
            else:
                current = choice(nextlist)
            current_points = points(current)
            temperature -= dT
