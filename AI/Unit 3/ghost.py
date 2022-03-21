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
def gameOver(word):
    if word in myDict:
        return 1
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


def negamax_step(word, alpha, beta, dic): 
    if word in visited:
        return None
    visited.add(word)
    score = gameOver(word)
    if score == 1:
        return score # if the word is complete, current player loses
    results = list()
    possible, newDic = possibleLetters(word, dic)
    for letter in possible:
        newWord = word + letter
        results.append(-1*negamax_step(newWord, -beta, -alpha, newDic)) #run the algorithm again with the opposite player
        alpha = max(alpha, m:=max(results))
        if alpha >= beta:
            break
    return m

def negamax_move(word, dic):
    score = gameOver(word)
    if score == -1:
        return score # if the word is complete, current player loses
    results = dict()
    results[-1] = set()
    results[1] = set()
    possible, newDic = possibleLetters(word, dic)
    for letter in possible:
        newWord = word + letter
        results[-1*negamax_step(newWord, -sys.maxsize, sys.maxsize, newDic)].add(letter)
    return results[1]

if len(n:=negamax_move(startWord, myDict)) == 0:
    print("Next player will lose!")
else:
    print('Next player can guarantee victory by playing any of these letters: ', list(n))
