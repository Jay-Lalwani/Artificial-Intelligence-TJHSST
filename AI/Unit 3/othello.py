import sys
import time

#Name: Jay Lalwani

   # Based on whether player is x or o, start an appropriate version of minimax

   # that is depth-limited to "depth".  Return the best available move.

def possible_moves(board, token):
    possible = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1,1), (1, -1), (-1, 1), (-1, -1)]
    for i, t in enumerate(board):
        if t == token:
            index = i
            for d in directions:
                soFar = set()
                row = index // 8
                column = index % 8
                while row >= 0 and row <8 and column >= 0 and column < 8 :
                    if row*8 + column != index:
                        if board[row*8 + column] == '.':
                            if len(soFar) == 0 or '.' in soFar or token in soFar:
                                break
                            else:
                                possible.add(row*8+column)
                                break
                        soFar.add(board[row*8 + column])
                    row += d[0]
                    column += d[1]
    return list(possible)


def make_move(board, token, index):
    board = board[:index] + token + board[index+1:]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1,1), (1, -1), (-1, 1), (-1, -1)]
    
    for d in directions:
                soFar = set()
                soFarIndex = set()
                row = index // 8
                column = index % 8
                while row >= 0 and row <8 and column >= 0 and column < 8 :
                    if row*8 + column != index:
                        if board[row*8 + column] == token:
                            if len(soFar) == 0 or '.' in soFar or token in soFar:
                                break
                            else:
                                for i in soFarIndex:
                                    board = board[:i] + token + board[i+1:]
                                break
                        soFar.add(board[row*8 + column])
                        soFarIndex.add(row*8+column)
                    row += d[0]
                    column += d[1]      
    return board
'''def make_move(board, token, index):
    board = board[:index] + token + board[index+1:]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1,1), (1, -1), (-1, 1), (-1, -1)]
    possible = dict()
    for d in directions:
        possible[d] = list()
        row = index // 8
        column = index % 8
        while row >= 0 and row <8 and column >= 0 and column < 8 :
            if board[row*8+column] == '.':
                break
            possible[d].append(row*8 + column)
            row += d[0]
            column += d[1]

    toFlip = []
    for p in possible.keys():
        for i, q in enumerate(possible[p]):
            if q != index:
                if board[q]==token:
                    tR = {board[i] for i in possible[p][1:i]}
                    tP = possible[p][1:i]
                    if '.' not in tR and token not in tR:
                        toFlip += tP
                    break
                        
    for tile in toFlip:
        board = board[:tile] + token + board[tile+1:]
    return board'''




# All your other functions
def gameOver(board, player):
    
    if player=='x':
        opposite='o'
    else: opposite = 'x'
    c=-1
    if board.count(".") == 0:
        c= -1  # -1 is game over
    if (myPossible:= len(possible_moves(board, player))) > 0:
        c= 0  # current player takes a turn
    if (yourPossible:= len(possible_moves(board, opposite))) > 0:
        c= 0  # other player gets a turn


      # -1 is game over here too; only will get here if both players are stuck
    myB=board.count(player)
    yourB= board.count(opposite)


    if c==-1:
        if (myB) > (yourB):
             return True, 10000 + 10*(myB-yourB)
        else: return True, -1*(10000+10*(myB-yourB))
    else: 

        s = 0
        s += myPossible
        s -= yourPossible
        
        corners = {0: (1, 9, 8), 7: (6, 14, 15), 56: (48, 49, 57), 63: (62, 54, 55)}
        for corner, adjacent in corners.items():
            if (b:= board[corner]) == player:
                s += 100
                for i in adjacent:
                    if board[i] == player:
                        s += 20
                    elif board[i] == opposite:
                        s-=20
            elif b== opposite:
                s -= 100
                '''for i in adjacent:
                    if board[i] == player:
                        s += 10
                    elif board[i] == opposite:
                        s -= 10'''
            else:
                for i in adjacent:
                    if board[i] == player:
                        s -= 20
                    elif board[i] == opposite:
                        s += 20
                '''for moves in yourp:
                    if board[moves] not in corners[corner]:
                        dontAdd = False
                        break
                if dontAdd:
                    s += 100'''
        

        return False, s

def negamax_step(board, playerVal, depth, alpha, beta): 
    if playerVal == 'x': #playerVal --> X is 1, O is -1
        opposite = 'o'
    else: opposite = 'x'
    game, score = gameOver(board, playerVal)
    if game or depth==0:
        return score # if player is X it is 1 x score, else if the player is O it is -1 x score
    if len(p:=possible_moves(board, playerVal)) == 0:
        return -1*negamax_step(board, opposite, depth, -1*beta, -1*alpha)
    results = list()
    for nextBoard in p:
        newBoard = make_move(board, playerVal, nextBoard)
        results.append(-1*negamax_step(newBoard, opposite, depth-1, -1*beta, -1*alpha)) #run the algorithm again with the opposite player
        #AB Pruning HERE
        alpha = max(alpha, m:=max(results))
        if alpha > beta:
            return m
    return m

def find_next_move(board, playerVal, depth):

    if playerVal == 'x': #playerVal --> X is 1, O is -1
        opposite = 'o'
    else: opposite = 'x'
    game, score = gameOver(board, playerVal)
    if game:
        return score # if player is X it is 1 x score, else if the player is O it is -1 x score
    results = dict()
    for nextBoard in possible_moves(board, playerVal):
        newBoard = make_move(board, playerVal, nextBoard) 
        results[-1*negamax_step(newBoard, opposite, depth, -10000000, 10000000)] = nextBoard#check every possible board to see the other player's possiblity to win, lose, or draw
    return results[max(results.keys())] #we return the board where the other player's possibility to win is the least so we use min()

class Strategy():

   logging = True  # Optional

   def best_strategy(self, board, player, best_move, still_running):

       depth = 1
        
       for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all
           
           best_move.value = find_next_move(board, player, depth)
           print(depth, best_move.value)
           depth += 1
'''
results = []
with open("boards_timing.txt") as f:
    for line in f:
        board, token = line.strip().split()
        temp_list = [board, token]
        print(temp_list)
        for count in range(1, 7):
            print("depth", count)
            start = time.perf_counter()
            find_next_move(board, token, count)
            end = time.perf_counter()
            temp_list.append(str(end - start))
        print(temp_list)
        print()
        results.append(temp_list)
with open("boards_timing_my_results.csv", "w") as g:
    for l in results:
        g.write(", ".join(l) + "\n")
sys.exit()

board = sys.argv[1]
#board = '.....................o...ooooo..xxxxoox.ooooooo.................'
#player = 'x'
player = sys.argv[2]

depth = 1

for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all
   print(find_next_move(board, player, depth))
   #print(time.perf_counter(), "seconds")
   depth += 1'''
