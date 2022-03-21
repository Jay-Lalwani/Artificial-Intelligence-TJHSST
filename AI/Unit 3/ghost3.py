import sys

file = sys.argv[1]
n = int(sys.argv[2])

startWord = ''
if len(sys.argv) == 4:
    startWord = sys.argv[3].strip().upper()

myDict = set()
with open(file) as f:
    for word in f:
        if len(word.strip()) >= n and word.strip().isalpha():
            myDict.add(word.strip().upper())

visited = set()
def gameOver(word, player):
    if word in myDict:
        if player == 0:
            return 1
        else: return -1
    else:
        return 0

def possibleLetters(word, dic):
    possible = set()
    newDic = set()
    length = len(word)
    for words in dic:
        if words[:length] == word:
            possible.add(words[length])
            newDic.add(words)
    return possible, newDic


def negamax_step(word, dic, player): 
    if word in visited:
        return None
    visited.add(word)
    score = gameOver(word, player)
    if score == 1 or score == -1:
        return score # if the word is complete, current player loses
    results = list()
    possible, newDic = possibleLetters(word, dic)
    for letter in possible:
        newWord = word + letter
        results.append(negamax_step(newWord, newDic, (player+1)%3)) #run the algorithm again with the opposite player
    return max(results)

def negamax_move(word, dic):
    score = gameOver(word, 0)
    if score == 1:
        return score # if the word is complete, current player loses
    results = dict()
    results[-1] = set()
    results[1] = set()
    possible, newDic = possibleLetters(word, dic)
    for letter in possible:
        newWord = word + letter
        results[negamax_step(newWord, newDic, 0)].add(letter)
    return results[-1]

if len(n:=negamax_move(startWord, myDict)) == 0:
    print("Next player will lose!")
else:
    print('Next player can guarantee victory by playing any of these letters: ', sorted(list(n)))
