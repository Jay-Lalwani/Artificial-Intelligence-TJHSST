import sys
import time
import random

n = 31

def create_board():
    return random.sample(range(n), n)

board = create_board()

def goal_test(board):
    return -1 not in board

def csp_backtracking(state):
    if goal_test(state): 
        return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var):
        new_state = state.copy()
        new_state[var] = val
        result = csp_backtracking(new_state)
        if result is not None:
            return result
    return None

def get_next_unassigned_var(board):
    while True:
        temp = random.randint(0, n-1)
        if board[temp] == -1:
            return temp

def get_sorted_values(board, index):
    notPossible = set()
    for row, position in enumerate(board):
        if position != -1:
            notPossible.add(position)
            rowDiff = index - row
            notPossible.add(position + rowDiff)
            notPossible.add(position - rowDiff)
    possible = [i for i in range(n) if i not in notPossible]
    return possible


def getConflicts(board, index):
    conflicts = set()
    for row, position in enumerate(board):
        rowDiff = index - row
        if board[index] == position or board[index] == position + rowDiff or board[index] == position - rowDiff:
            conflicts.add(row)
    conflicts.remove(index)
    return conflicts

def totalAndMaxConflicts(board):
    conflictsCount = 0
    max = [-1, -1]

    for i in range(len(board)):
        conflictsCount += (c:= len(getConflicts(board, i)))

        if c > max[0]:
            max = [c, i]
        elif c == max[0]:
            max.append(i)

    maxRandom = random.choice(max[1:])

    return (conflictsCount, maxRandom)
      

def incrementalRepair(board):
    total, max = totalAndMaxConflicts(board)
    while total > 0:
        min = [sys.maxsize, -1]
        for pos in range(n):
            new_state = board.copy()
            new_state[max] = pos
            if (c:=len(getConflicts(new_state, max))) < min[0]:
                min = [c, pos]
            elif c == min[0]:
                min.append(pos)
        minRandom = random.choice(min[1:])
        board[max] = minRandom
        total, max = totalAndMaxConflicts(board)
    return board

def fastSolution(num):
    even = [i for i in range(num) if i % 2 == 0] #0, 2, 4, 6 for 8x8
    odd = [i for i in range(num) if i % 2 != 0] #1, 3, 5, 7 for 8x8

    if num % 6 == 2:
        return odd + even[1::-1] + even[3:] + [even[2]]
    elif num % 6 == 3:
        return  odd[1:] + [odd[0]] + even[2:] + even[0:2]
    else:
        return odd+even



def test_solution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
        for compare in range(var + 1, len(state)):
            left -= 1
            right += 1
            if state[compare] == middle:
                print(var, "middle", compare)
                return False
            if left >= 0 and state[compare] == left:
                print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right:
                print(var, "right", compare)
                return False
    return True
'''
start = time.perf_counter()
solutions = list()
n=8
now = 0.0
while n <= 200 and now < 30.0:
    solutions.append(fastSolution(n))
    now = time.perf_counter()
    n+=1

end = time.perf_counter()

for solution in solutions:
    print(test_solution(solution))
print('Total time to solve puzzles of n=8 to n=200:', end - start, 'seconds')'''