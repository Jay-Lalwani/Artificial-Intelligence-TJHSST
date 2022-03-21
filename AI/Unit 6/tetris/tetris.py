from lib2to3.pgen2.token import STAR
from statistics import mean
import sys
import random
import pickle



inpBoard = '                                                                                                                                                                                               #########'


def translate(boardString):
    temp = [boardString[idx: idx + 10] for idx in range(0, len(boardString), 10)]
    matrix = [list(ele) for ele in temp]
    return matrix

def toString(matrix):
    s = ''
    for i in matrix:
        for j in i:
            s += j
    return s

def printBoard(boardString):
    print("=======================")
    for count in range(20):
        print(' '.join(list(("|" + boardString[count * 10: (count + 1) * 10] + "|"))), " ", count)
    print("=======================")
    print()
    print("  0 1 2 3 4 5 6 7 8 9  ")
    print()


pieces = {'I': ['00.10.20.30', '00.01.02.03'], 'O': ['00.01.10.11'], 'T': ['00.10.20.11', '00.01.02.11', '01.10.11.21', '01.10.11.12'], 'S': ['00.10.11.21', '01.02.11.10'], 'Z': ['01.10.11.20', '00.01.11.12'], 'J':['00.01.10.20', '00.01.02.12', '01.11.21.20', '00.10.11.12'], 'L':['00.10.20.21','00.10.01.02','00.01.11.21','02.12.11.10']}


def highestPosition(matrix, location): 
    for row in range(20):
        if matrix[row][location] == '#':
            return row
    return 20

def place(boardString, rotation, location):
    matrix = translate(boardString)
    highest = highestPosition(matrix, location)
    if rotation == '02.12.11.10':
        highest += 1
    toReplace = []
    positions = rotation.split('.')
    for row, i in enumerate(matrix):
        if row <= highest:
            toReturn = False
            for pos in positions:
                y = int(pos[0])
                x = int(pos[1])
                if row >= (highest - 1) and (row-x) < 0:
                    toReplace.append(-1)
                    toReturn = False
                    break
                if (location+y) >= 10 or matrix[row-x][location+y] == '#':
                    toReturn = False
                    break
                toReturn = True
            if toReturn:
                toReplace.append(row)
    if not toReplace:
        return 0
    gameOver = True
    for r in toReplace:
        if r != -1:
            gameOver = False
            break
    if gameOver:
        return -1
    else:
        row = max(toReplace)
        for pos in positions:
            y = int(pos[0])
            x = int(pos[1])
            matrix[row-x][location+y] = '#'
        deleted = []
        for index, row in enumerate(matrix):
            if ' ' not in row:
                deleted.append(index)
        p = len(deleted) #reminder: 1 row cleared --> 40 points, 2 --> 100, 3 --> 300, 4 --> 1200
        if p==0:
            points=0
        elif p == 1:
            points = 40
        elif p==2:
            points = 100
        elif p==3:
            points = 300
        elif p==4:
            points = 1200
        for d in deleted:
            for i in range(d, 0, -1):
                matrix[i] = matrix[i-1]
            matrix[0] = [' ' for j in range(10)]

        return (toString(matrix), points)



#test = sys.argv[1]
test = "          #         #         #      #  #      #  #      #  #     ##  #     ##  #     ## ##     ## #####  ########  ######### ######### ######### ######### ########## #### # # # # ##### ###   ########"
# with open("tetrisout2.txt", 'a') as t:
#     t.truncate(0)
#     for piece in pieces:
#         for rotation in pieces[piece]:
#             for i in range(10):
#                 if (p:=place(test, rotation, i)) == -1:
#                     t.write('GAME OVER\n')
#                 elif p == 0:
#                     None
#                 else:
#                     printBoard(p[0])
#                     input() 
#                     t.write(p[0] + '\n')
# sys.exit()
def heuristicCalculations(matrix):
    highest = [20 for i in range(10)]
    numHoles = 0
    for location in range(10):
        for row in range(20):
            if matrix[row][location] == '#':
                if row < highest[location]:
                    highest[location] = row
                if row < 19 and matrix[row+1][location] == ' ':
                    r = row+1
                    while r < 20 and matrix[r][location] == ' ':
                        numHoles+=1
                        r += 1
    bumpiness = 0
    for h in range(len(highest)-1):
        bumpiness += abs(highest[h] - highest[h+1])
    return min(highest), max(highest), numHoles, bumpiness


def heuristic(board, points, strategy):
    matrix = translate(board)
    a, b, c, d, e = strategy # As many variables as you want!
    col, well, hol, bump = heuristicCalculations(matrix)
    value = 0
    value += a * col       # highest column height
    value += b * well      # well depth
    value += c * hol      # number of holes 
    value += d * points    # points scored from recent placement
    value += e * bump      # bumpiness of adjacent columns

    

    return value

def makeBoard():
    board = [' ' for i in range(200)]
    board = ''.join(board)
    return board

def play_game(strategy):
    board = makeBoard()
    points = 0
    while True:
        possBoardsAndScores = []
        piece = random.sample(list(pieces.keys()), 1)[0]
        for rotation in pieces[piece]:
            for location in range(10):
                poss_board = place(board, rotation, location)
                if poss_board == 0:
                    continue
                elif poss_board == -1:
                    possBoardsAndScores.append((-1000000, (board, -1)))
                else:
                    poss_score = heuristic(poss_board[0], poss_board[1], strategy)
                    possBoardsAndScores.append((poss_score, poss_board))
                    
                # Keep track of the board with the highest heuristic score however you like!
        if len(possBoardsAndScores) ==0:
            break
        board = max(possBoardsAndScores)
        if board[0] == -1000000:
            break
        points += board[1][1] 
        board = board[1][0]
    return points  


def play_game_with_print(strategy):
    board = makeBoard()
    points = 0
    while True:
        printBoard(board)
        possBoardsAndScores = []
        piece = random.sample(list(pieces.keys()), 1)[0]
        for rotation in pieces[piece]:
            for location in range(10):
                poss_board = place(board, rotation, location)
                if poss_board == 0:
                    continue
                elif poss_board == -1:
                    possBoardsAndScores.append((-1000000, (board, -1)))
                else:
                    poss_score = heuristic(poss_board[0], poss_board[1], strategy)
                    possBoardsAndScores.append((poss_score, poss_board))
                    
                # Keep track of the board with the highest heuristic score however you like!
        if len(possBoardsAndScores) ==0:
            break
        board = max(possBoardsAndScores)
        if board[0] == -1000000:
            break
        points += board[1][1] 
        board = board[1][0]
    return points

POPULATION_SIZE = 200
NUM_CLONES = 50
TOURNAMENT_SIZE = 10
TOURNAMENT_WIN_PROBABILITY = .75
MUTATION_RATE = .8
STRATEGY_SIZE = 5
NUM_TRIALS = 5


def createPop(): #returns a list of strategies
    gen0 = set()
    while len(gen0) < POPULATION_SIZE:
         gen0.add(tuple([random.uniform(-1, 1) for i in range(STRATEGY_SIZE)]))
    return list(gen0)

def fitness(strategy):
    game_scores = []
    for count in range(NUM_TRIALS):
        game_scores.append(play_game(strategy))
    return mean(game_scores)

def fitPop(population):
    oldPop = []
    for index, strategy in enumerate(population):
        oldPop.append((f:=fitness(strategy), strategy))
        print('Evaluating strategy number', index, end=' --> ')
        print(f)
    oldPop = sorted(oldPop)[::-1]
    return oldPop

def breed(parents):
    parent1 = parents[0][1]
    parent2 = parents[1][1]
    numRandom = random.randint(1, STRATEGY_SIZE-1)
    child = [i for i in range(STRATEGY_SIZE)]
    p1 = set(random.sample(child, numRandom))
 
    for i in p1:
        child[i] = parent1[i]
    for i in range(STRATEGY_SIZE):
        if i not in p1:
            child[i] = parent2[i]

    if random.random() < MUTATION_RATE:
        mutation = random.sample(range(len(child)), 1)[0]
        child[mutation] = child[mutation] + random.uniform(-0.2, 0.2)

    return tuple(child)

def selectAndBreed(oldPop):
    nextGen = set()
    for i in range(NUM_CLONES):
        nextGen.add(oldPop[i][1])
    while len(nextGen) != POPULATION_SIZE:
        tournaments = random.sample(oldPop, 2*TOURNAMENT_SIZE)
        tournament1 = sorted(tournaments[:TOURNAMENT_SIZE])[::-1]
        tournament2 = sorted(tournaments[TOURNAMENT_SIZE:])[::-1]
        parents = []
        while not parents:
            if len(tournament1) == 1 or random.random() < TOURNAMENT_WIN_PROBABILITY:
                parents.append(tournament1[0])
            else: tournament1 = tournament1[1:]
        while len(parents) == 1:
            if len(tournament2) == 1 or random.random() < TOURNAMENT_WIN_PROBABILITY:
                parents.append(tournament2[0])
            else: tournament2 = tournament2[1:]
        child = breed(parents)
        nextGen.add(child)
    nextGen = list(nextGen)
    return nextGen

def loadSaved(filename):
    infile = open(filename, 'rb')
    gen, pop = pickle.load(infile)
    infile.close()
    return (gen, pop)

def savePop(population, filename): #population is actually (gen, population)
    outfile = open(filename, 'wb')
    pickle.dump(population, outfile)
    outfile.close()

def geneticAlgorithm():
    i = 0
    print('(N)ew process, or (L)oad saved process?', end=' ')
    newOrSaved = input()
    if newOrSaved.upper() == 'N':
        gen0 = createPop()
        nextGen = fitPop(gen0)
    elif newOrSaved.upper() == 'L':
        print('What filename?', end = ' ')
        file = input()
        i, nextGen = loadSaved(file)
        i -= 1
    else: sys.exit(1)
    print("Average:", mean(n[0] for n in nextGen))
    print("Generation:", i)
    print("Best strategy so far:", nextGen[0][1], 'with score:', nextGen[0][0])
    while True:
        i+= 1
        print('(P)lay a game with current best strategy, (S)ave current process, or (C)ontinue?', end=' ')
        bestOrSaveOrContinue = input()
        if bestOrSaveOrContinue.upper() == 'C':
            nextGen = fitPop(selectAndBreed(nextGen))
            print("Average:", mean(n[0] for n in nextGen))
            print("Generation:", i)
            print("Best strategy so far:", nextGen[0][1], 'with score:', nextGen[0][0])
        elif bestOrSaveOrContinue.upper() == 'P':
            print('Points scored:', play_game_with_print(nextGen[0][1]))
            i -= 1
        elif bestOrSaveOrContinue.upper() == 'S':
            print('What filename?', end = ' ')
            file = input()
            savePop((i, nextGen), file)
            sys.exit(0)
        else: continue

geneticAlgorithm()