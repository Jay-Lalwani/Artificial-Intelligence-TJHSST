import sys

dfaTest = open(sys.argv[3]).read().split('\n')
regex = sys.argv[1] #a|(ab|b*a)*
alphabet = sys.argv[2] #ab

def regexToNFAwe(regex):
    nfa = {0: {regex: 1}}
    final = [1]
    nextNode = 2
    for char in regex:
        if char in alphabet:





def dfaRun(dfaInp):
    numStates = int(dfaInp[1])
    final = dfaInp[2].split(' ')
    final = list(map(int, final))

    dfa = {}
    for i in range(numStates):
        dfa[i] = {}

    temp = -1
    for inp in dfaInp[3:]:
        if inp == '':
            temp += 1
        if len(inp) > 1:
            inOut = inp.split(' ')
            dfa[temp][inOut[0]] = int(inOut[1])
    return dfa

def dfaPrint(dfa, alphabet):
    print("*", end = "\t")
    for a in alphabet:
        print(a, end="\t")
    print()
    for state in dfa:
        print(state, end="\t")
        for a in alphabet:
            if a not in dfa[state].keys():
                char = r"_"
            else:
                char = dfa[state][a]
            print(char, end="\t")
        print()

def dfaEmulator(dfa, inp, final):
    state = 0
    for i in inp:
        if i not in dfa[state].keys():
            return False
        else:
            state = dfa[state][i]

    return state in final




dfaPrint(dfa, alphabet)
print("Final nodes:", final)
for inp in dfaTest:
    print(dfaEmulator(dfa, inp, final), inp)
