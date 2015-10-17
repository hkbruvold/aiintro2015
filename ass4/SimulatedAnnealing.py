#! /usr/bin/env python3


from math import exp

class SimulatedAnnealing:
    """ Implementiation of the general algorithm"""
    
    def __init__(self, start_board, temp_func, variation_board, points_func):
        t=1
        current = start_board
        while t == 1:
            temperature= temp_func(t)
            if temperature = 0:
                return current
            nextt= random.variation_board()
            evaluation = points_func(variation_board) - points_func(current)
            if evaluation>0:
                current = variation_board
            else:
                prob = exp(evaluation/temperature)
                current = variation_board
                
                
                
            
            
            
        
        
        
