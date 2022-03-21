import sys

def isPrime(x):
    if x == 2: return True
    elif x < 2: return False
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(x**0.5) + 1, 2):
            if x % i == 0: return False
        return True

#Question 1
print("Q1", sum({i for i in range(1000) if i % 3 == 0 or i % 5 == 0}))

#Question 2
listD = [1, 1]
for i in range(2, 100000):
    if listD[-1] > 4000000:
        listD = listD[:-1]
        break
    listD.append(listD[i-2]+listD[i-1])
print("Q2", sum({i for i in listD if i % 2 == 0}))

#Question 3
temp = []
x = 600851475143
i=2
max = 1
while i < x**(1/2):
    if 600851475143 % i == 0 and isPrime(i):
        temp.append(i)
        i+=1
    else:
        x//i
        i+=1
print("Q3", temp[-1])

#Question 4
temp4 = -1
s = ""
for i in range(100, 1000):
    for j in range(100, 1000):
        s = str(i*j)
        if s == s[::-1]:
            if i*j > temp4:
                temp4 = i*j

print("Q4", temp4)

#Question 5
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

list5 = [i for i in range(0, 21)]
list5[0] = 1
for ind in range(1,21):
    list5[0] = (list5[ind]*list5[0]) // gcd(list5[0], list5[ind])

print("Q5", list5[0])

#Question 6
print("Q6", (sum([i6 for i6 in range(1, 101)])**2) - sum([i6**2 for i6 in range(1, 101)]))

#Question 7
count7 = 0
i7 = 1
while count7 <= 10000:
    if isPrime(i7):
        count7+=1
    i7 += 1
print("Q7", i7-1)

#Question 8
n8 = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
max8 = 0
for i8 in range(len(s8 := str(n8))-13):
    if (temp8 := int(s8[i8])*int(s8[i8+1])*int(s8[i8+2])*int(s8[i8+3])*int(s8[i8+4])*int(s8[i8+5])*int(s8[i8+6])*int(s8[i8+7])*int(s8[i8+8])*int(s8[i8+9])*int(s8[i8+10])*int(s8[i8+11])*int(s8[i8+12])) > max8:
        max8 = temp8

print("Q8", max8)

#Question 9
for a9 in range(1, 1000):
    for b9 in range(1, 1000):
        c9 = (a9**2 + b9**2)**0.5
        if a9 < b9 < c9 and a9 + b9 + c9 == 1000:
            total9 = int(a9*b9*c9)
            break
print("Q9", total9)

#Question 29
print("Q29", len({i29**j29 for i29 in range(2, 101) for j29 in range(2, 101)}))