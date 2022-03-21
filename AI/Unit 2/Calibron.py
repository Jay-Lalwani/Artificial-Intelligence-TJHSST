import sys



# You are given code to read in a puzzle from the command line.  The puzzle should be a single input argument IN QUOTES.
# A puzzle looks like this: "56 56 28x14 32x11 32x10 21x18 21x18 21x14 21x14 17x14 28x7 28x6 10x7 14x4"
# The code below breaks it down:
puzzle = sys.argv[1].split()
#puzzle = "56 56 28x14 32x11 32x10 21x18 21x18 21x14 21x14 17x14 28x7 28x6 10x7 14x4".split()
puzzle_height = int(puzzle[0])
puzzle_width = int(puzzle[1])
rectangles = [(int(temp.split("x")[0]), int(temp.split("x")[1])) for temp in puzzle[2:]]
# puzzle_height is the height (number of rows) of the puzzle
# puzzle_width is the width (number of columns) of the puzzle
# rectangles is a list of tuples of rectangle dimensions

N = int(puzzle_height*puzzle_width)

# INSTRUCTIONS:
#
# First check to see if the sum of the areas of the little rectangles equals the big area.
# If not, output precisely this - "Containing rectangle incorrectly sized."
def printCalibron(state):
    for i in range(N):
        print(state[i], end=' ')
        if (i+1) % (puzzle_width) == 0:
            print()
def sizeCheck():
    area = puzzle_height * puzzle_width
    rectAreas = 0
    for dim in rectangles:
        rectAreas += (dim[0]*dim[1])
    return area == rectAreas

if sizeCheck() == False:
    print("Containing rectangle incorrectly sized.")
    sys.exit(0)

# Then try to solve the puzzle.
# If the puzzle is unsolvable, output precisely this - "No solution."
board = [-1 for i in range(N)]


def goal_test_calibron(state):
    return -1 not in state

def coord(pos):
    row = pos // puzzle_width
    column = pos % puzzle_width
    return (row, column)

def csp_backtracking_calibron(state, myRect, solutionSet):
    if goal_test_calibron(state): 
        return state, solutionSet
    var = get_next_unassigned_var_calibron(state)
    for val in get_sorted_values_calibron(state, var, myRect):
        new_state = state.copy()
        new_rect = myRect.copy()
        new_state = assign(new_state, var, val[0], val[1], val[2])
        new_rect[val[2]] = -1
        new_sol = solutionSet.copy()
        new_sol.append((var, val[0], val[1]))
        result = csp_backtracking_calibron(new_state, new_rect, new_sol)
        if result is not None:
            return result
    return None

def get_next_unassigned_var_calibron(state):
    return state.index(-1)

def createBlock_calibron(index, height, width):
    block = list()
    for j in range(index, index+width):
        for k in range(0, puzzle_width*height, puzzle_width):
            block.append(j+k)
    return block


def assign(state, index, height, width, value):
    for i in createBlock_calibron(index, height, width):
        state[i] = value
    return state

def checkBlock(state, index, height, width):
    for i in createBlock_calibron(index, height, width):
        if i > (N-1):
            return False
        if state[i] != -1:
            return False
    return True

def get_sorted_values_calibron(state, index, myRect):
    possible = list()
    for i, rect in enumerate(myRect):
        if(rect == -1):
            continue
        height = rect[0]
        width = rect[1]
        if checkBlock(state, index, height, width):
            possible.append((height, width, i))
        
        #flipped
        height = rect[1]
        width = rect[0]
        if checkBlock(state, index, height, width):
            possible.append((height, width, i))
    return possible
            
if (toReturn := csp_backtracking_calibron(board, rectangles, list())) is None:
    print("No solution.")
    sys.exit(0)
solutionBoard, solution = toReturn
printCalibron(solutionBoard)
for s in solution:
    rc = coord(s[0])
    r = rc[0]
    c = rc[1]
    h = s[1]
    w = s[2]
    print(r, c, h, w)

# If the puzzle is solved, output ONE line for EACH rectangle in the following format:
# row column height width
# where "row" and "column" refer to the rectangle's top left corner.
#
# For example, a line that says:
# 3 4 2 1
# would be a rectangle whose top left corner is in row 3, column 4, with a height of 2 and a width of 1.
# Note that this is NOT the same as 3 4 1 2 would be.  The orientation of the rectangle is important.
#
# Your code should output exactly one line (one print statement) per rectangle and NOTHING ELSE.
# If you don't follow this convention exactly, my grader will fail.