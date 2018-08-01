from pfp import *
import random
import math

def allUnique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)

def unfoldState(state, n):
    seq = []
    print(state)
    spaces = [0,0,0,0]
    while(state > 1):
        actionToAppend = int(state % 4)
        seq.append(actionToAppend)
        if ((state - 1) % 4 == 0): action = 4
        else: action = (state - 1) % 4
        state = (state + 3 - action)/4
        print(state)
    seq.append(int(state % 4))
    seq.reverse()
    seq = seq[:(n-1)]
    for i in seq:
        spaces[i] = spaces[i] + 1
    print("Sequenza di azioni:", seq)
    #print("spazi:", spaces)
    numSeq = []
    prev = spaces[2] + n*spaces[3]
    numSeq.append(prev)
    for i in seq:
        up = prev - n
        down = prev + n
        left = prev - 1
        right = prev + 1
        if i == 0:
            numSeq.append(right)
            prev = right
        elif i == 1:
            numSeq.append(down)
            prev = down
        elif i == 2:
            numSeq.append(left)
            prev = left
        else:
            numSeq.append(up)
            prev = up
    #print("Sequenza prima della traslazione: ", numSeq)
    minBound = min(numSeq)
    if(minBound < 0): numSeq = [i - min(numSeq) for i in numSeq]
    #print("Sequenza dopo la traslazione: ", numSeq)
    return numSeq

def isFinal(state, n):
    return state > ((4**(n-1) - 1)/3)

def isValid(seq): return allUnique(seq)

def energy(seq, primary):
    printTertiary(fillMatrix(seq, primary))
    return score(fillMatrix(seq, primary), countH(primary)[3])

def transition(state, action):
    #print("da stato", state, "a succ: ", (state * 4) - 3 + actionDict[action], "con l'azione", action, " - ", actionDict[action])
    return (state * 4) - 3 + actionDict[action]

def reward(state, action, n, primary):
    result = transition(state, action)
    if(not isValid(unfoldState(result, n))):
        #print("Stato non valido")
        return 0.01
    elif(isFinal(result, n)):
        print("Stato finale valido con energia: ", energy(unfoldState(result, n), primary))
        return energy(unfoldState(result, n), primary)
    else:
        return 0.1

def Qf(state, action, n, discountFactor, Q, primary):
    currRew = reward(state, action, n, primary)
    nextSpace = transition(state, action)
    futureRew = 0
    for i in actionSpace:
        rew = 0
        if (nextSpace, i) in Q:
            rew = Q[(nextSpace, i)]
        if(rew > futureRew): futureRew = rew
    return currRew + discountFactor * futureRew

primary = "HHPH"
n = len(primary)
#print(n)
startState = 1
actionSpace = ['L', 'U', 'R', 'D']
actionDict = {'L' : 1, 'U' : 2, 'R' : 3, 'D' : 4}
discountFactor = 0.9
episodes = 36

Q = {}

print("=== Begin training ===")

for i in range(episodes):
    state = startState
    while(not isFinal(state, n)):
        maxRew = 0
        maxAct = random.choice(actionSpace)
        for i in actionSpace:
            rew = Qf(state, i, n, discountFactor, Q, primary)
            if(rew > maxRew):
                maxRew = rew
                maxAct = i
        explorer = random.choice(actionSpace)
        act = random.choice([maxAct, explorer])
        Q[(state, act)] = Qf(state, act, n, discountFactor, Q, primary)
        state = transition(state, act)

for key in sorted(Q):
    print "%s: %s" % (key, Q[key])

print("=== End training === \n === ==== ===")
print("=== Start testing ===")

state = startState
while(not isFinal(state, n)):
    print(state)
    maxRew = 0
    rew = 0
    maxAct = random.choice(actionSpace)
    for i in actionSpace:
        if (state, i) in Q:
            rew = Q[(state, i)]
        if(rew > maxRew):
            maxRew = rew
            maxAct = i
    print("AZIONE", maxAct)
    print("RICOMPENSA", maxRew)
    state = transition(state, maxAct)
seq = unfoldState(state, n)
print(seq)
print("=== Configurazione trovata ===")
printTertiary(fillMatrix(seq, primary))
print("=== Energia della configurazione ===", score(fillMatrix(seq, primary), countH(primary)[3]))
