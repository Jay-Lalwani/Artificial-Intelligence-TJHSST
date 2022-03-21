import sys
import time
from collections import deque
from heapq import heappush, heappop, heapify

puzzle = """ 1 2 3 3 4 .
             1 2 5 5 4 .
             0 0 6 7 . .
             . . 6 7 8 .
             . . . 7 8 .
             . . . . . .

"""  # 0 = red car, every proceeding number is another car/truck

vehicles = [(2, "horizontal", 11), (2, "vertical", 0)] # vehicles is a list of all vehicles in order of their car number, and stored as a tuple of (length, direction, position); ex: vehicles[0][2] == 11

def coord(l, char):
    pos = l.index(char) + 6
    row = pos // 6
    col = pos % 6
    return (row, col)

def goal_test(l, red):
    return coord(l, red) == (2, 4)

def move(board, length, direction, carNumber, moveDistance):
    coordinates = coord(board, carNumber)
    if direction == 'vertical':
        if moveDistance > 0:
            if (coordinates[0] + length - 1 + moveDistance) < 6:
                
        else: 
            if (coordinates[0] + moveDistance) >= 0:

    else: # direction == horizonatal

