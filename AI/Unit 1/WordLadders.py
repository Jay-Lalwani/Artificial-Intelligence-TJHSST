import sys
import time
from collections import deque

with open(sys.argv[1]) as f:
    words = {line.strip() for line in f}

with open(sys.argv[2]) as g:
    line_list = [line2.strip() for line2 in g]

puzzles = [i.split() for i in line_list]

start = time.perf_counter()

wordDict = dict()
template = dict()

for word in words:
    for cIndex in range(len(word)):
        temp = word[0: cIndex] + '.' + word[cIndex+1:]
        if temp not in template:
            template[temp] = set()
        template[temp].add(word)

for x in template:
    for a in template[x]:
        for b in template[x]:
            if b != a:
                if b not in wordDict:
                    wordDict[b] = set()
                wordDict[b].add(a)
end = time.perf_counter()

print()
print("Time to create the data structure was:", t1:=(end - start), "seconds")
print("There are", len(words), "words in this dict.")
print()

def bfs(start, end):
    if(start not in words or end not in words):
        return "No Solution!"
    fringe = deque()
    visited = {start}
    fringe.append((start, 1, [start]))
    while len(fringe) > 0:
        v, count, path = fringe.popleft()
        if v == end:
            return count, path
        for c in wordDict[v]:
            if c not in visited:
                fringe.append((c, count+1, path + [c]))
                visited.add(c)
    return "No Solution!"

def bfsQ2(start):
    fringe = deque()
    visited = set()
    fringe.append((start))
    visited.add(start)
    countQ2 = 0
    while len(fringe) > 0:
        v= fringe.popleft()
        countQ2 += 1
        for c in wordDict[v]:
            if c not in visited:
                fringe.append((c))
                visited.add(c)
    return countQ2

def bfsQ3(start):
    if start not in wordDict:
        return -1
    fringe = deque()
    visited = set()
    fringe.append((start))
    visited.add(start)
    while len(fringe) > 0:
        v = fringe.popleft()
        for c in wordDict[v]:
            if c not in visited:
                fringe.append((c))
                visited.add(c)
    return visited

def bfsQ4(l):
    fringe = deque()
    visited = set()
    fringe.append((l, 1))
    visited.add(l)
    highest = -1
    toReturn = ""
    while len(fringe) > 0:
        v, count = fringe.popleft()
        if count > highest:
            highest = count
            toReturn = v
        for c in wordDict[v]:
            if c not in visited:
                fringe.append((c, count+1))
                visited.add(c)
    return toReturn, highest

x = []

start2 = time.perf_counter()

for puzzle in puzzles:
    x.append(bfs(puzzle[0], puzzle[1]))

end2 = time.perf_counter()

for index in range(len(x)):
    print("Line:", index)
    if x[index] == "No Solution!":
        print("No Solution!")
    else:
        print("Length is:", x[index][0])
        for solution in x[index][1]:
            print(solution)
    print()

print("Time to solve all these puzzles was:", t2:=(end2 - start2), "seconds")
print()
print("Total Runtime:", t1 + t2)

'''Questions 1-4
#1
count1 = 0
for word in words:
    if word not in wordDict:
        count1 += 1
print(count1)

#2
print(bfsQ2("willed"))

#3
countQ3 = 0
allClumps = []
for word in words:
    if bfsQ3(word) not in allClumps and bfsQ3(word) != -1:
        allClumps.append(bfsQ3(word))
print(len(allClumps))

#4
#print(bfsQ4("drifts"))
print("start: vaguer", "end: drifts", bfs("vaguer", "drifts"))'''