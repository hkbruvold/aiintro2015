#! /usr/bin/env python

import copy
import assignment5 as ass


boards = ["easy.txt", "medium.txt", "hard.txt", "veryhard.txt"]


for board in boards:
    csp = ass.create_sudoku_csp("sudokus/%s" %(board))
    
    print "Solving %s" %(board)
    solution = csp.backtracking_search()
    ass.print_sudoku_solution(solution)
    print "backtrack count: ", csp.backtrack_count
    print "backtrack fail count: ", csp.backtrack_failure_count
    print


