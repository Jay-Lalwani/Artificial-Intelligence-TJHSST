import sys
import time
from collections import deque
from heapq import heappush, heappop, heapify
import tkinter as tk
from math import pi , acos , sin , cos

def calcd(node1, node2):
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees
   if node1 == node2:
      return 0
      
   y1, x1 = node1
   y2, x2 = node2

   R   = 3958.76 # miles = 6371 km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0

   # approximate great circle distance with law of cosines
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

datastart = time.perf_counter()

with open("rrNodeCity.txt") as f:
    cityID = {line.strip()[8:]  :  line.strip()[:7] for line in f}

with open("rrNodes.txt") as g:
    idPos = {line.strip()[:7]  :  (float(line.strip()[8:17]), float(line.strip()[18:])) for line in g}


with open("rrEdges.txt") as h:
    rr = dict()
    for line in h:
        a = line.strip()[:7]
        b = line.strip()[8:]
        d = calcd(idPos[a], idPos[b])
        if a not in rr:
            rr[a] = set()
        rr[a].add((b, d))
        if b not in rr:
            rr[b] = set()
        rr[b].add((a, d))

dataend = time.perf_counter()

print("Time to create data structure:", dataend - datastart, "seconds")

lines = dict() #list of all the lines created

def create_grid(c):
    for i in rr.keys():
        for j in rr[i]:
            y1, x1 = idPos[i]
            y2, x2 = idPos[j[0]]
            line = c.create_line([(50 + (x1+130)*10, 700 - y1*10), (50 + (x2+130)*10, 700 - y2*10)], tag='grid_line')
            lines[(i, j[0])] = line

updateCount = 0
def make_color(r, c, a, b, color, n): #makes all the lines red
        c.itemconfig(lines[(a, b)], fill= color, width = "4")
        global updateCount
        if updateCount % n == 0:
            r.update() #update frame
        updateCount += 1
        #time.sleep(0.1)

def reset(r, c):
    for line in lines.values():
        c.itemconfig(line, fill="black", width = "1")
    r.update()
    

root = tk.Tk() #creates the frame

canvas = tk.Canvas(root, height=800, width=800, bg='white') #creates a canvas widget, which can be used for drawing lines and shapes
create_grid(canvas)
canvas.pack(expand=True) #packing widgets places them on the board


#root.mainloop()




def dijkstra(a, b):
    idA = cityID[a]
    idB = cityID[b]

    path = list()
    path.append(idA)
    closed = set()
    fringe = []
    heappush(fringe, (0, (idA, 0), path))

    while len(fringe) > 0:
        depth, v, p = heappop(fringe)
        if v[0] == idB:
            reset(root, canvas)
            for i in range(len(p) - 1):
                make_color(root, canvas, p[i], p[i+1], "green", 200)
            return depth
        if v[0] not in closed:
            closed.add(v[0])
            for c in rr[v[0]]:
                if c[0] not in closed:
                    heappush(fringe, (depth + c[1], c, p + [c[0]])) 
                    make_color(root, canvas, v[0], c[0], "red", 2000)
    

    return None

def a_star(a, b):
    idA = cityID[a]
    idB = cityID[b]
    
    closed = set()
    fringe = []
    path = list()
    path.append(idA)
    heappush(fringe, (calcd(idPos[idA], idPos[idB]), 0, (idA, 0), path))

    while len(fringe) > 0:
        f, depth, v, p = heappop(fringe)
        if v[0] == idB:
            reset(root, canvas)
            for i in range(len(p) - 1):
                make_color(root, canvas, p[i], p[i+1], "green", 200)
            return depth
        if v[0] not in closed:
            closed.add(v[0])
            for c in rr[v[0]]:
                if c[0] not in closed:
                    heappush(fringe, (depth + c[1] + calcd(idPos[c[0]], idPos[idB]), depth + c[1], c, p + [c[0]]) )
                    make_color(root, canvas, v[0], c[0], "blue", 500)

                  
    return None




a = sys.argv[1]
b = sys.argv[2]

dstart = time.perf_counter()
dlength = dijkstra(a, b)
dend = time.perf_counter()

print(a, "to", b, "with Dijkstra:", dlength, "in", dend-dstart, "seconds.")

root.mainloop()
time.sleep(0.1)
root = tk.Tk()

canvas = tk.Canvas(root, height=800, width=800, bg='white') #creates a canvas widget, which can be used for drawing lines and shapes
create_grid(canvas)
canvas.pack(expand=True)
reset(root, canvas)

astart = time.perf_counter()
alength = a_star(a, b)
aend = time.perf_counter()

print(a, "to", b, "with A*:", alength, "in", aend-astart, "seconds.")
root.mainloop()
time.sleep(0.1)
