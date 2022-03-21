
from colorama import init, Back, Fore  
import re
import sys

init()  

inp = sys.argv[1]

inp = inp.split('/')[1:]


if len(inp[1]) == 0:
    exp = re.compile(inp[0])
else:
    flags = 0
    for f in inp[1]:
        if f == 'i':
            f
        elif f== 'm':
           f = re.M
        elif f=='s':
           f = re.S
        flags |= f
    
    exp = re.compile(inp[0], flags)
s= '''
Singing in the rain
  is bringing me joy.'''
#s = "While inside they wined and dined, safe from the howling wind.\nAnd she whined, it seemed, for the 100th time, into the ear of her friend,\nWhy indeed should I wind the clocks up, if they all run down in the end?"

highlights = [Back.LIGHTYELLOW_EX, Back.LIGHTCYAN_EX]
indexes = []
for result in exp.finditer(s):
    indexes.append(result.span())
    

print(indexes)

prevEnd = 0
hIndex = 0
toPrint = ''
if len(indexes) != 0:
    ending = s[indexes[-1][1]:]
else: ending = s

for start, end in indexes:
    if prevEnd != 0 and start == prevEnd:
        hIndex = (hIndex + 1) %2
    else: hIndex = 0
    toPrint = toPrint + s[prevEnd:start] + highlights[hIndex] + s[start:end] + Back.RESET
    prevEnd = end

toPrint += ending

print(toPrint)

