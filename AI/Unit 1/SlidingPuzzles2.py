import sys
import time
from collections import deque
from heapq import heappush, heappop, heapify


with open(sys.argv[1]) as f:
    line_list = [line.strip() for line in f]

line = [i.split()[1] for i in line_list]
num = [int(i.split()[0]) for i in line_list]
method = [i.split()[2] for i in line_list]

def print_puzzle(l, n):
    for i in range(len(l)):
        print(l[i], end='  ')
        if((i + n + 1) % n == 0):
            print('\n')

def find_goal(l):
    return ''.join(sorted(l)[1:]) + '.'

def switch(l, a, b):
    temp = list(l)
    temp[b] = l[a]
    temp[a] = l[b]
    return ''.join(temp)

def get_children(l, n):
    children = []
    location = l.index('.')
    if location+n < len(l):
        children.append(switch(l, location, location+n))
    if location-n >= 0:
        children.append(switch(l, location, location-n))
    if location+1 < len(l) and (location+1+n) % n != 0:
        children.append(switch(l, location, location+1))
    if location-1 >= 0 and (location+n) % n != 0:
        children.append(switch(l, location, location-1))
    return children

def goal_test(l):
    return l == find_goal(l)

def parityCount(l):
    temp = l.replace('.', '')
    count = 0
    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            if temp[j] < temp[i]:
                count+=1
    return count


def parityCheck(l, n):
    if n%2 == 0:
        if 0 < ((l.index('.') + 2*n + 1) % (2*n)) <= n:
            return (parityCount(l) % 2 != 0)
        else:
            return (parityCount(l) % 2 == 0)   
    else:
        return (parityCount(l) % 2 == 0)

def coord(l, char, n):
    pos = l.index(char) + n
    row = pos // n
    col = pos % n
    return (row, col)

def taxiCab(l, n, goal):
    totalDistance = 0
    for char in l:
        if char != '.':
            totalDistance += (abs(coord(l, char, n)[0] - (coord(goal, char, n)[0])) + abs(coord(l, char, n)[1] - (coord(goal, char, n)[1])))
    return totalDistance

def kDFS(l, k, n):
    fringe = deque()
    fringe.append((l, 0, {l}))

    while len(fringe) > 0:
        v, depth, visited = fringe.pop()
        if goal_test(v):
            return depth
        if depth < k:
            for c in get_children(v, n):
                if c not in visited:
                    tempV = visited.copy()
                    tempV.add(c)
                    fringe.append((c, depth+1, tempV))
    return None

def idDFS(l, n):
    maxDepth = 0
    result = None
    while result is None:
        result = kDFS(l, maxDepth, n)
        maxDepth += 1
    return result

def aStar(l, n):
    goal = find_goal(l)
    closed = set()
    fringe = []
    heappush(fringe, (taxiCab(l, n, goal), 0, l))

    while len(fringe) > 0:
        f, depth, v = heappop(fringe)
        if v == goal:
            return depth
        if v not in closed:
            closed.add(v)
            for c in get_children(v, n):
                if c not in closed:
                    heappush(fringe, (depth + taxiCab(c, n, goal), depth + 1, c))
    return None


def bfs(l, n):
    fringe = deque()
    visited = set()
    fringe.append((l, 0))
    visited.add(l)
    while len(fringe) > 0:
        v, count = fringe.popleft()
        if goal_test(v):
            return count
        for c in get_children(v, n):
            if c not in visited:
                fringe.append((c, count+1))
                visited.add(c)
    return None

for i in range(len(line)):
    linput = line[i]
    ninput = num[i]
    
    if method[i] == 'A':
        start = time.perf_counter()

        if parityCheck(linput, ninput):
            toPrint = aStar(linput, ninput)
        else:
            toPrint = "no solution"

        end = time.perf_counter()

        if toPrint == "no solution":
            print("Line %s" % i + ":", linput + ', no solution determined in ', end= "")
        else:
            print("Line %s" % i + ":", linput + ', A* - ', toPrint, "moves found in ", end= "")
        print(end - start, "seconds")

    elif method[i] == 'B':
        start = time.perf_counter()

        if parityCheck(linput, ninput):
            toPrint = bfs(linput, ninput)
        else:
            toPrint = "no solution"

        end = time.perf_counter()

        if toPrint == "no solution":
            print("Line %s" % i + ":", linput + ', no solution determined in ', end= "")
        else:
            print("Line %s" % i + ":", linput + ', BFS - ', toPrint, "moves found in ", end= "")
        print(end - start, "seconds")
    
    elif method[i] == 'I':
        start = time.perf_counter()

        if parityCheck(linput, ninput):
            toPrint = idDFS(linput, ninput)
        else:
            toPrint = "no solution"

        end = time.perf_counter()

        if toPrint == "no solution":
            print("Line %s" % i + ":", linput + ', no solution determined in ', end= "")
        else:
            print("Line %s" % i + ":", linput + ', ID-DFS - ', toPrint, "moves found in ", end= "")
        print(end - start, "seconds")
    
    else:
        

        start = time.perf_counter()

        if parityCheck(linput, ninput):
            toPrint = bfs(linput, ninput)
        else:
            toPrint = "no solution"

        end = time.perf_counter()

        if toPrint == "no solution":
            print("Line %s" % i + ":", linput + ', no solution determined in ', end= "")
        else:
            print("Line %s" % i + ":", linput + ', BFS - ', toPrint, "moves found in ", end= "")
        print(end - start, "seconds")
    
        start = time.perf_counter()

        if parityCheck(linput, ninput):
            toPrint = idDFS(linput, ninput)
        else:
            toPrint = "no solution"

        end = time.perf_counter()

        if toPrint == "no solution":
            print("Line %s" % i + ":", linput + ', no solution determined in ', end= "")
        else:
            print("Line %s" % i + ":", linput + ', ID-DFS - ', toPrint, "moves found in ", end= "")
        print(end - start, "seconds")

        start = time.perf_counter()
 
        if parityCheck(linput, ninput):
            toPrint = aStar(linput, ninput)
        else:
            toPrint = "no solution"

        end = time.perf_counter()

        if toPrint == "no solution":
            print("Line %s" % i + ":", linput + ', no solution determined in ', end= "")
        else:
            print("Line %s" % i + ":", linput + ', A* - ', toPrint, "moves found in ", end= "")
        print(end - start, "seconds")
    print()
    



    
