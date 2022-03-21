import sys

puzzle = sys.argv[1]

rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
columns = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
diagonals = [[0, 4, 8], [2, 4, 6]]

wins = rows+columns+diagonals


def gameOver(board, playerVal):
    filled = False
    if '.' not in board:
        filled = True
    for win in wins:
        if board[win[0]] == 'X' or board[win[0]] == 'O':
            if board[win[0]] == board[win[1]] == board[win[2]]:
                toReturn = 1 if board[win[0]] == playerVal else -1
                return True, toReturn
    if filled:
        return True, 0
    return False, None

def possibleBoards(board, c):
    possible = list()
    for space in range(9):
        if board[space] == '.':
            temp = board[:space] + c + board[space+1:]
            possible.append(temp)
    return possible

def possibleBoardIndexes(board):
    possible = list()
    for space in range(9):
        if board[space] == '.':
            possible.append(str(space))
    return possible

def max_step(board):
    game, score = gameOver(board)
    if game:
        return score
    results = list()
    for nextBoard in possibleBoards(board, 'X'):
        results.append(min_step(nextBoard))
    return max(results)

def min_step(board):
    game, score = gameOver(board)
    if game:
        return score
    results = list()
    for nextBoard in possibleBoards(board, 'O'):
        results.append(max_step(nextBoard))
    return min(results)

def max_move(board):
    game, score = gameOver(board)
    if game:
        return score
    results = dict()
    for nextBoard in possibleBoards(board, 'X'):
        results[nextBoard] = min_step(nextBoard)
    return list(results.keys())[list(results.values()).index(max(results.values()))]

def min_move(board):
    game, score = gameOver(board)
    if game:
        return score
    results = dict()
    for nextBoard in possibleBoards(board, 'O'):
        results[nextBoard] = max_step(nextBoard)
    return list(results.keys())[list(results.values()).index(min(results.values()))]


def negamax_step(board, playerVal): 
    if playerVal == 'X': #playerVal --> X is 1, O is -1
        opposite = 'O'
    else: opposite = 'X'

    game, score = gameOver(board, playerVal)
    if game:
        return score # if player is X it is 1 x score, else if the player is O it is -1 x score
    results = list()
    for nextBoard in possibleBoards(board, playerVal): 
        results.append(-1*negamax_step(nextBoard, opposite)) #run the algorithm again with the opposite player
    return max(results)

def negamax_move(board, playerVal):
    if playerVal == 'X': #playerVal --> X is 1, O is -1
        opposite = 'O'
    else: opposite = 'X'
    game, score = gameOver(board, playerVal)
    if game:
        return score # if player is X it is 1 x score, else if the player is O it is -1 x score
    results = dict()
    for nextBoard in possibleBoards(board, playerVal):
        results[nextBoard] = -1*negamax_step(nextBoard, opposite) #check every possible board to see the other player's possiblity to win, lose, or draw
    return list(results.keys())[list(results.values()).index(max(results.values()))] #we return the board where the other player's possibility to win is the least so we use min()




def printBoard(board):
    print('Current Board:')
    print(board[0:3] + '    ' + '012')
    print(board[3:6] + '    ' + '345')
    print(board[6:9] + '    ' + '678')
    print()



def changedIndex(old, new):
    for i in range(9):
        if old[i] != new[i]:
            return i
    return -1
    

if puzzle == '.........':
    empty = True
else:
    empty = False

if empty:
    print('Should I be X or O?', end = " ")
    myPlayer = input()
    turn = 'X'
else:
    if puzzle.count('X') == puzzle.count('O'):
        myPlayer = 'X'
        turn = 'X'
    else:
        myPlayer = 'O'
        turn = 'O'
if myPlayer == 'X': 
        opposite = 'O'
else: opposite = 'X'
print()
printBoard(puzzle)

while gameOver(puzzle, myPlayer)[0] == False:
    oldPuzzle = puzzle
    if turn == myPlayer:
        for i in possibleBoardIndexes(puzzle):
            k = negamax_step(puzzle[:int(i)] + turn + puzzle[int(i)+1:], opposite)
            if k == 1:
                k = 'loss.'
            elif k == -1:
                k = 'win.'
            else: k = 'tie.'
            print('Moving  at', i, 'results in a', k)
        print()
        print('I choose space', changedIndex(oldPuzzle, p:=negamax_move(puzzle, myPlayer)), end='.\n')
        puzzle = p

    else:
        print('You can move to any of these spaces:', (', '.join(possibleBoardIndexes(puzzle)) + '.'))
        print("Your choice?", end = " ")
        space = int(input())
        while space < 0 or space > 8 or puzzle[space] != '.':
            print("Your choice?", end = " ")
            space = int(input())
        puzzle = puzzle[:space] + turn + puzzle[space+1:]

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    print()
    printBoard(puzzle)

if (g:=gameOver(puzzle, myPlayer)[1]) == 1:
    winner = myPlayer
elif g == -1:
    winner = opposite
else:
    print('We tied!')
    sys.exit(0)
if winner == myPlayer:
    print('I win!')
else: print('You win!')