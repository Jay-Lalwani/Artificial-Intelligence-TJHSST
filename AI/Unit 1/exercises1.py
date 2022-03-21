import sys

if sys.argv[1] == "A":
    print(int(sys.argv[2]) + int(sys.argv[3]) + int(sys.argv[4]))
if sys.argv[1] == "B":
    sumB = 0
    for i in range(2, len(sys.argv)):
        sumB += int(sys.argv[i])
    print(sumB)
if sys.argv[1] == "C":
    listC = [int(sys.argv[i]) for i in range(2, len(sys.argv)) if int(sys.argv[i]) % 3 == 0]
    print(listC)
if sys.argv[1] == "D":
    listD = [1, 1]
    for i in range(2, int(sys.argv[2])):
        listD.append(listD[i-2]+listD[i-1])
    print(listD)
if sys.argv[1] == "E":
    listE = [i**2 -3*i + 2 for i in range(int(sys.argv[2]), int(sys.argv[3]) + 1)]
    print(listE)
        
if sys.argv[1] == "F":
    listF = [float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])]
    if listF[0] + listF[1] <= listF[2] or listF[1] + listF[2] <= listF[0] or listF[0] + listF[2] <= listF[1]:
        print("Error")
    else:
        s = sum(listF) / 2
        print((s*(s-listF[0])*(s-listF[1])*(s-listF[2]))**(1/2))
if sys.argv[1] == "G":
    dict = {"a":0, "e":0, "i":0, "o":0, "u":0}
    for char in sys.argv[2]: 
        if char.lower() in dict:
            dict[char.lower()] += 1

    print(dict)

