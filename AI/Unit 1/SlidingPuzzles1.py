import sys
import time
from collections import deque

with open(sys.argv[1]) as f:
    line_list = [line.strip() for line in f]

line = [i.split()[1] for i in line_list]
num = [int(i.split()[0]) for i in line_list]

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



def bfs(l, n):
    fringe = deque()
    visited = set()
    fringe.append((l, 0))
    visited.add(l)
    while len(fringe) > 0:
        v, count = fringe.popLeft()
        if goal_test(v):
            return count
        for c in get_children(v, n):
            if c not in visited:
                fringe.append((c, count+1))
                visited.add(c)
    return None
    

def bfspath(l, n):
    fringe = deque()
    visited = set()
    list1 = list()
    fringe.append((l, list1))
    visited.add(l)
    while len(fringe) > 0:
        v, count = fringe.popleft()
        if goal_test(v):
            return count

        for c in get_children(v, n):
            if c not in visited:
                fringe.append((c, count + [c]))
                visited.add(c)
    return None

def reversebfs(l, n):
    fringe = deque()
    visited = set()
    fringe.append((l, 0))
    visited.add(l)
    highest = 31
    toReturn = list()
    while len(fringe) > 0:
        v, count = fringe.popleft()
        if count == highest:
            toReturn.append(v)
        for c in get_children(v, n):
            if c not in visited:
                fringe.append((c, count+1))
                visited.add(c)
    return toReturn

def bibfs(l, n):
    
    fringedown = deque()
    visiteddown = set()

    l2 = find_goal(l)
    fringeup = deque()
    visitedup = set()

    fringedown.append((l, 0))
    visiteddown.add(l)

    fringeup.append((l2, 0))
    visitedup.add(l2)

    while len(fringeup) and len(fringedown) > 0:
        v1, count1 = fringedown.popleft()
        v2, count2 = fringeup.popleft()

        if goal_test(v1):
            return count1

        for c in get_children(v1, n):
            if c not in visiteddown:
                fringedown.append((c, count1+1))
                visiteddown.add(c)
                for index1 in range(len(fringeup)):
                    if c == fringeup[index1][0]:
                        temp1 = dict(fringeup)
                        return temp1[c] + count1 + 1
       
        for c in get_children(v2, n):
            if c not in visitedup:
                fringeup.append((c, count2+1))
                visitedup.add(c)
                for index2 in range(len(fringedown)):
                    if c == fringedown[index2][0]:
                        temp2 = dict(fringedown)
                        return temp2[c] + count2 + 1
    return None

'''6
for node in reversebfs("12345678.", 3):
    print(node)
    print(bfspath(node,3))
    print(bfs(node,3))
    print()'''

for i in range(len(line)):
    linput = line[i]
    ninput = num[i]

    print(parityCheck(linput, ninput))
    
    start = time.perf_counter()

    toPrint = bfs(linput, ninput)

    end = time.perf_counter()
    print("Line %s" % i + ":", linput + ',', toPrint, "moves found in ", end= "")
    print(end - start, "seconds")

    start2 = time.perf_counter()

    toPrint = bibfs(linput, ninput)

    end2 = time.perf_counter()
    print("Line %s" % i + ":", linput + ',', toPrint, "moves found in ", end= "")
    print(end2 - start2, "seconds with biBFS")
