import sys

dfaTest = open(sys.argv[2]).read().split('\n')

if sys.argv[1].isnumeric():
    if sys.argv[1] == '1':    #1
        dfa = {0: {'a': 1}, 1: {'a': 2}, 2: {'b': 3}, 3:{}}
        alphabet = 'ab'
        final = [3]
    elif sys.argv[1] == '2':    #2
        dfa = {0: {'0': 0, '1': 1, '2': 0}, 1: {'0': 0, '1': 1, '2': 0}}
        alphabet = '012'
        final = [1]
    elif sys.argv[1] == '3':     #3
        dfa = {0: {'a': 0, 'b': 1, 'c': 0}, 1: {'a': 1, 'b': 1, 'c': 1}}
        alphabet = 'abc'
        final = [1]
    elif sys.argv[1] == '4':     #4
        dfa = {0: {'0': 1, '1': 0}, 1: {'0': 0, '1': 1}}
        alphabet = '01'
        final = [0]
    elif sys.argv[1] == '5':     #5
        dfa = {0: {'0': 2, '1': 1}, 1: {'0': 3, '1': 0}, 2: {'0': 0, '1': 3}, 3: {'0': 1, '1': 2}} 
        #0 is even 0 even 1, 1 is even 0 odd 1, 2 is odd 0 even 1, 3 is odd 0 odd 1
        alphabet = '01'
        final = [0]
    elif sys.argv[1] == '6':     #6
        dfa = {0: {'a': 1, 'b': 0, 'c': 0}, 1: {'a': 1,'b': 2, 'c': 0}, 2: {'a': 1, 'b': 0,'c': 3}, 3:{}}
        alphabet = 'abc'
        final = [0, 1, 2]
    elif sys.argv[1] == '7':     #7
        dfa = {0: {'0': 0, '1': 1}, 1: {'0': 2, '1': 1}, 2: {'0': 2, '1': 3}, 3: {'0': 2, '1': 4}, 4:{'0': 4, '1': 4}}
        alphabet = '01'
        final = [4]
    else: sys.exit(1)
else:
    dfaInp = open(sys.argv[1]).read().split('\n')
    alphabet = dfaInp[0]
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
