
import re
import sys
vowels = {'a', 'e', 'i', 'o', 'u'}
 

inp = sys.argv[1]
file = open(inp)
dic = file.read().lower()
words = dic.split('\n')

print("#1:",r'''re.compile(r"^(?=\w*a)(?=\w*e)(?=\w*i)(?=\w*o)(?=\w*u)\w*$", re.I | re.M)''')
exp1 = re.compile(r"^(?=\w*a)(?=\w*e)(?=\w*i)(?=\w*o)(?=\w*u)\w*$", re.I | re.M)

match1 = 0
result1 =[]
for result in exp1.finditer(dic):
    result1.append((len(result[0]),result[0]))
    

result1 = sorted(result1)
size1 = result1[0][0]
count1 = 0
for r in result1:
    if r[0] == size1:
        match1+=1
    else:break
print(match1, "total matches")
for r in result1:
    if r[0] != size1 or count1 >= 5:
        break 
    print(r[1])
    count1 += 1


print()
print("#2:",r'''re.compile(r"^([b-df-hj-np-tv-z]*[aeiou]){5}[b-df-hj-np-tv-z]*$", re.I | re.M)''')


exp2 = re.compile(r"^([b-df-hj-np-tv-z]*[aeiou]){5}[b-df-hj-np-tv-z]*$", re.I | re.M)

match2 = 0
result2 =[]
for result in exp2.finditer(dic):
    result2.append((-1*len(result[0]),result[0]))
    

result2 = sorted(result2)

size2 = result2[0][0]
count2 = 0
for r in result2:
    if r[0] == size2:
        match2+=1
    else:break
print(match2, "total matches")
for r in result2:
    if r[0] != size2 or count2 >= 5:
        break 
    print(r[1])
    count2 += 1


print()
print("#3:",r'''re.compile(r"^(\w)((?!\1\w*\1\b)\w)*\1$", re.I | re.M)''')


exp3 = re.compile(r"^(\w)((?!\1\w*\1\b)\w)*\1$", re.I | re.M)

match3 = 0
result3 =[]
for result in exp3.finditer(dic):
    result3.append((-1*len(result[0]),result[0]))
    

result3 = sorted(result3)

size3 = result3[0][0]
count3 = 0
for r in result3:
    if r[0] == size3:
        match3+=1
    else:break
print(match3, "total matches")
for r in result3:
    if r[0] != size3 or count3 >= 5:
        break 
    print(r[1])
    count3 += 1
    
print()
print("#4:",r'''re.compile(r"^(?=(\w)(\w)(\w))(?=\w*\3\2\1\b)\w*$", re.I | re.M)''')


exp4 = re.compile(r"^(?=(\w)(\w)(\w))(?=\w*\3\2\1\b)\w*$", re.I | re.M)

match4 = 0
result4 =[]
for result in exp4.finditer(dic):
    result4.append(result[0])
    match4+=1
    

result4 = sorted(result4)

count4 = 0

print(match4, "total matches")
for r in result4:
    if count4 >= 5:
        break 
    print(r)
    count4 += 1
    
print()
print("#5:",r'''re.compile(r"^(?!(\w*b){2})(?!\w*t{2})\w*(bt|tb)\w*$", re.I | re.M)''')


exp5 = re.compile(r"^(?!(\w*b){2})(?!(\w*t){2})\w*(bt|tb)\w*$", re.I | re.M)

match5 = 0
result5 =[]
for result in exp5.finditer(dic):
    result5.append(result[0])
    match5+=1
    

result5 = sorted(result5)

count5 = 0

print(match5, "total matches")
for r in result5:
    if count5 >= 5:
        break
    print(r)
    count5 += 1
    

print()
print("#6:",r'''re.compile(r"(\w)\1+", re.I | re.M)''')


exp6 = re.compile(r"(\w)\1+", re.I | re.M)

match6 = 0
result6 = set()
for result in exp6.finditer(dic):
    result6.add(result[0])
    
max6 = -1
for r in result6:
    if len(r) > max6:
        max6 = len(r)
result6f = list()
for r in result6:
    if len(r) == max6:
        exp6 = re.compile(r"^\w*" + r + r"\w*$", re.I | re.M)
        for result in exp6.finditer(dic):
            result6f.append(result[0])
count6 = 0

result6f = sorted(result6f)
match6 = len(result6f)

print(match6, "total matches")
for r in result6f:
    if count6 >= 5:
        break
    print(r)
    count6 += 1
    
    
print()
print("#7:",r'''re.compile(r"^\w*(\w)(\w*\1\w*){"+ str(size7) + r"}$", re.I | re.M)''')


result7 = set()
result7.add("-1")
prev7 = set()
size7 = 2
while result7:
    prev7 = result7
    result7 = set()
    for result in re.compile(r"^\w*(\w)\w*(\1\w*){"+ str(size7) + r"}$", re.I | re.M).finditer(dic):
        result7.add(result[0])
    size7 += 1
result7f = sorted(prev7)
match7 = len(result7f)
count7 = 0
print(match7, "total matches")
for r in result7f:
    if count7 >= 5:
        break
    print(r)
    count7 += 1


print()
print("#8:",r'''re.compile(r"^(?=\w*(" + match + r"\w*){" + str(prev8f[0]) + r"})\w*$", re.I | re.M)''')
temp8 = ''
prev8 = [0]
for word in words:
    for index in range(len(word)-1):
        temp8 = word[index] + word[index+1]
        if word.count(temp8) > prev8[0]:
            prev8 = [word.count(temp8), temp8]
        elif word.count(temp8) == prev8[0]:
            prev8.append(temp8)

prev8f = []
for element in prev8:
   if element not in prev8f:
       prev8f.append(element)

result8 = set()
for match in prev8f[1:]:
    for result in re.compile(r"^(?=\w*(" + match + r"\w*){" + str(prev8f[0]) + r"})\w*$", re.I | re.M).finditer(dic):
        result8.add(result[0])

result8 = sorted(result8)
match8 = len(result8)
count8 = 0
print(match8, "total matches")
for r in result8:
    if count8 >= 5:
        break
    print(r)
    count8 += 1

print()
print("#9:",r'''re.compile(r"^\w*([b-df-hj-np-tv-z]\w*){"+ str(prev9) + r"}$", re.I | re.M)''')
temp9 = 0
prev9 = -1
for word in words:
    for letter in word:
        if letter.isalpha() and letter not in vowels:
            temp9 += 1
    if temp9 > prev9:
        prev9 = temp9
    temp9 = 0

result9 = set()

for result in re.compile(r"^\w*([b-df-hj-np-tv-z]\w*){"+ str(prev9) + r"}$", re.I | re.M).finditer(dic):
    result9.add(result[0])

result9 = sorted(result9)
match9 = len(result9)
count9 = 0
print(match9, "total matches")
for r in result9:
    if count9 >= 5:
        break
    print(r)
    count9 += 1


print()
print("#10:",r'''re.compile(r"^((\w)(?!\w*\2\w*\2))+$", re.I | re.M)''')

exp10 = re.compile(r"^((\w)(?!\w*\2\w*\2))+$", re.I | re.M)

match10 = 0
result10 = []
for result in exp10.finditer(dic):
    result10.append((-1*len(result[0]),result[0]))
    

result10 = sorted(result10)
size10 = result10[0][0]
count10 = 0
for r in result10:
    if r[0] == size10:
        match10+=1
    else:break
print(match10, "total matches")
for r in result10:
    if r[0] != size10 or count10 >= 5:
        break 
    print(r[1])
    count10 += 1

