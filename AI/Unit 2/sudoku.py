import sys
import time
import random

AtoG = "ABCDEFG"
with open(sys.argv[1]) as f:
   sudokuPuzzles = [line.strip() for line in f]

def calculations(s):
    n = int(len(s)**(1/2))
    
    sH = int(n**(1/2))
    while n % sH != 0:
        sH -= 1
    sW = n//sH

    symbols = set()
    
    if n <= 9:
        for i in range(1, n+1):
            symbols.add(str(i))
    else:
        for i in range(1, 10):
            symbols.add(str(i))
        for j in range(n-9):
            symbols.add(AtoG[j])

    return n, sW, sH, symbols

def printPuzzle(s):
    n, sW, sH, symbols = calculations(s)
    for p in range(n+1):
        print('---', end='')
    print()
    print(' | ', end='')
    for i in range(len(s)):
        print(s[i], end= ' ')
        if (i+1) % n == 0:
            print(' | ')
        if i == len(s) - 1:
            break
        if (i+1) % (sH*n) == 0:
            for p in range(n+1):
                print('---', end='')
            print()
        if (i+1) % sW == 0:
            print(' | ', end='')
    for p in range(n+1):
        print('---', end='')
    print()


def createRows(s):
    rows = list()

    n, sW, sH, symbols = calculations(s)

    for i in range(0, len(s), n):
        row = set()
        for j in range(n):
            row.add(i+j)
        rows.append(row)

    return rows

def createColumns(s):
    columns = list()

    n, sW, sH, symbols = calculations(s)

    for i in range(n):
        column = set()
        for j in range(0, len(s), n):
            column.add(i+j)
        columns.append(column)

    return columns

def createBlocks(s):
    blocks = list()

    n, sW, sH, symbols = calculations(s)

    blockIndex = list()
    for j in range(0, n*n, sH*n):
        for i in range(0, n, sW):
                blockIndex.append(i+j)

    for i in blockIndex:
        block = set()
        for j in range(i, i+sW):
            for k in range(0, n*sH, n):
                block.add(j+k)
        blocks.append(block)

    return blocks

def createConstraints(s):
    return createRows(s) + createColumns(s) + createBlocks(s)

def createNeighbors(s):
    neigh = dict()

    for square in range(len(s)):
        neigh[square] = set()
        for constraint in createConstraints(s):
            if square in constraint:
                for item in constraint:
                    if square != item:
                        neigh[square].add(item)
    return neigh

neighbors = createNeighbors(sudokuPuzzles[0])

def symbolCount(s):
    n, sW, sH, symbols = calculations(s)
    symbolDict = dict()
    for symbol in symbols:
        symbolDict[symbol] = s.count(symbol)
    return symbolDict

def goal_test(s):
    if len(k:=set(symbolCount(s).values())) == 1 and int(len(s)**(1/2)) in k:
        return True
    return False

def forward_goal_test(s):
    for value in s.values():
        if len(value) != 1:
            return False
    return True


def csp_backtracking(state):
    n, sW, sH, symbols = calculations(state)

    if goal_test(state): 
        return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var):
        new_state = state[:var] + val + state[var+1:]
        result = csp_backtracking(new_state)
        if result is not None:
            return result
    return None


def get_next_unassigned_var(board):
    return board.find('.')
    '''while True:
        temp = random.randint(0, n-1)
        if board[temp] == -1:
            return temp'''

def get_sorted_values(board, index):
    n, sW, sH, symbols = calculations(board)
    for constraint in neighbors[index]:
        if board[constraint] in symbols:
            symbols.remove(board[constraint])

    return (sorted(list(symbols)))

def constrainedBoard(s):
    newBoard = dict()
    for index, item in enumerate(s):
        if item == '.':
            newBoard[index] = ''.join(get_sorted_values(s, index))
        else:
            newBoard[index] = str(item)
    return newBoard

def mostConstrained(newBoard):
    minConstraints = sys.maxsize
    index = -1
    for key in newBoard.keys():
        if (t:=len(newBoard[key])) > 1 and t < minConstraints:
            minConstraints = t
            index = key
    return index


def forwardLooking(newBoard):
    solved = list()
    for key, value in newBoard.items():
        if len(value) == 1:
            solved.append((key, value))
    for index in solved:
        global neighbors
        for constraint in neighbors[index[0]]:
            indexOfVal = newBoard[constraint].find(index[1])
            if indexOfVal != -1:
                temp = newBoard[constraint]
                newBoard[constraint] = temp[:indexOfVal] + temp[indexOfVal+1:]
                if (l:=len(newBoard[constraint])) == 1:
                    solved.append((constraint, newBoard[constraint]))
                elif l==0:
                    return None
    return newBoard

def cspforwardLooking(state, symbols):
    if forward_goal_test(state): 
        return state
    var = mostConstrained(state)
    for val in state[var]:
        new_state = state.copy()  
        new_state[var] = val
        checkedBoard = forwardLooking(new_state)
        tempBoard = dict()
        while checkedBoard is not None and checkedBoard != tempBoard:
            tempBoard = checkedBoard
            checkedBoard = toReturnConstraintPropagation(checkedBoard, symbols)
            if checkedBoard is not None:
                checkedBoard = forwardLooking(checkedBoard)
        if checkedBoard is not None:
            result = cspforwardLooking(checkedBoard, symbols)
            if result is not None:
                return result
    return None

def toReturnCspForwardLooking(state):
    n, sW, sH, symbols = calculations(state)
    newBoard = constrainedBoard(state)
    newBoard = forwardLooking(newBoard)
    return ''.join(cspforwardLooking(newBoard, symbols).values())

def constraintPropagation(state, constraint, symbols):
    for symbol in symbols:
        symbolCount = list()
        for index in constraint:
            if symbol in state[index]:
                symbolCount.append(index)
        if len(symbolCount) == 1:
            state[symbolCount[0]] = symbol
        elif len(symbolCount) == 0:
            return None
    return state

def toReturnConstraintPropagation(state, symbols):
    rows = createRows(state)
    columns = createColumns(state)
    blocks = createBlocks(state)

    newState = state
    for row in rows:
        newState = constraintPropagation(newState, row, symbols)
        if newState is None:
            return None
    for column in columns:
        newState = constraintPropagation(newState, column, symbols)
        if newState is None:
            return None
    for block in blocks:
        newState = constraintPropagation(newState, block, symbols)
        if newState is None:
            return None
    return newState
print(toReturnConstraintPropagation(constrainedBoard('.912..5....54........3.89.4.3....1.515.....292.9....3.9.86.7........46....2..149.'), '123456789'))
sys.exit()

for sudoku in sudokuPuzzles:
    if len(sudoku) != len(neighbors):
        neighbors = createNeighbors(sudoku)
    printPuzzle(toReturnCspForwardLooking(sudoku))