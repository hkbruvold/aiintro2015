#! /usr/bin/env python3


from math import exp
from random import random

class SimulatedAnnealing:
    """Implementiation of the general algorithm"""
    
    def run(self, start_board, temp_func, variation_board, points_func):
        """
        Runs the simmulated annealing algorithm. 
        Will run till temperature is 0 or a perfect solution is obtained
           
        Arguments:
        start_board: The initial board object
        temp_func: A function to calculate temperature from a given time t
        variation_board: A function that returns a neighbouring board
        points_func: A function to calculate (negative) points for a board"""
        
        t = 0
        current = start_board
        current_points = points_func(start_board)
        while True:
            temperature = temp_func(t)
            if temperature == 0:
                return current
            next = variation_board(current)
            ## positive evaluation is better choice
            next_points = points_func(next)
            if next_points == 0:
                return next
            evaluation = current_points - next_points
            if evaluation > 0:
                current = next
            else:
                prob = exp(evaluation/temperature)
                if prob >= random():
                    current = next
            t += 1
                  
