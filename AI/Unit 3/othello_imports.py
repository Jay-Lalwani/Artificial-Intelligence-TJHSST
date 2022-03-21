
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
