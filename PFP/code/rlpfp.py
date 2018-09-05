from pfp import *
from numpy.random import choice
import random
import math

actionSpace = ['L', 'U', 'R', 'D']
actionDict = {'L' : 1, 'U' : 2, 'R' : 3, 'D' : 4}
discountFactor = 0.9
episodes = 36

""" checks if all element of a list are unique """
def allUnique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)

""" from a given state, build the correspondent sequence """
def unfoldState(state, n):
    seq = []
    #print(state)
    spaces = [0,0,0,0]
    while(state > 1):
        #print("State", state)
        actionToAppend = int(state % 4) # action ordering (top - down)
        #print("Action to append", actionToAppend)
        seq.append(actionToAppend)
        if ((state - 1) % 4 == 0): action = 4
        else: action = (state - 1) % 4
        state = (state + 3 - action)/4
    seq.reverse() # action ordering (bottom - up)
    for i in seq:
        spaces[i] = spaces[i] + 1
    #print("spazi:", spaces)
    numSeq = []
    prev = spaces[2] + n*spaces[3]
    #print("Sequenza", seq)
    numSeq.append(prev)
    for i in seq:
        #print("Resto:", i)
        up = prev - n
        down = prev + n
        left = prev - 1
        right = prev + 1
        if i == 0:
            #print("R")
            numSeq.append(right)
            prev = right
        elif i == 1:
            #print("D")
            numSeq.append(down)
            prev = down
        elif i == 2:
            #print("L")
            numSeq.append(left)
            prev = left
        else:
            #print("U")
            numSeq.append(up)
            prev = up
    #print("Sequenza prima della traslazione: ", numSeq)
    minBound = min(numSeq)
    if(minBound < 0): numSeq = [i - min(numSeq) for i in numSeq]
    #print("Sequenza dopo la traslazione: ", numSeq)
    return numSeq

""" checks if a given state is final """
def isFinal(state, n):
    return state > ((4**(n-1) - 1)/3)

""" checks if a sequence is valid """
def isValid(seq): return allUnique(seq)

""" returns the energy of a configuration """
def energy(seq, primary):
    #printTertiary(fillMatrix(seq, primary))
    return score(fillMatrix(seq, primary), countH(primary)[3])

""" applies a transition to a state """
def transition(state, action):
    #print("da stato", state, "a succ: ", (state * 4) - 3 + actionDict[action], "con l'azione", action, " - ", actionDict[action])
    return (state * 4) - 3 + actionDict[action]

""" returns the reward for the pair (state, action) """
def reward(state, n, primary):
    if(not isValid(unfoldState(state, n))):
        #print("Stato non valido")
        return -0.01
    elif(isFinal(state, n)):
        #print("Stato finale valido con energia: ", energy(unfoldState(state, n), primary))
        return energy(unfoldState(state, n), primary)
    else:
        #print("Avanti")
        return 0.1

""" Qf function - returns the current reward and future reward of a given state """
def Qf(state, action, n, discountFactor, Q, primary):
    nextSpace = transition(state, action)
    currRew = reward(nextSpace, n, primary)
    futureRew = 0
    for i in actionSpace:
        if (nextSpace, i) in Q:
            rew = Q[(nextSpace, i)]
            if(rew > futureRew): futureRew = rew
    #print("futureRew", futureRew)
    total = currRew + (discountFactor * futureRew)
    #print(total)
    return total

def QL(primary):
    n = len(primary)
    startState = 1

    Q = {}

    print("TRAINING...")

    for i in range(episodes):
        state = startState
        while(not isFinal(state, n)):
            maxRew = 0
            for i in actionSpace:
                rew = Qf(state, i, n, discountFactor, Q, primary)
                if(rew > maxRew):
                    maxRew = rew
                    maxAct = i
            explorer = random.choice([x for x in actionSpace if x != maxAct])
            act = choice([maxAct, explorer], 1, p=[0.7,0.3])[0]
            Q[(state, act)] = Qf(state, act, n, discountFactor, Q, primary)
            state = transition(state, act)

    #for key in sorted(Q):
        #print "%s: %s" % (key, Q[key])

    print("TEST...")

    state = startState
    while(not isFinal(state, n)):
        #print(state)
        maxRew = 0
        for i in actionSpace:
            if(state, i) in Q:
                rew = Q[(state, i)]
            if(rew > maxRew):
                maxRew = rew
                maxAct = i
        #print("AZIONE", maxAct, "RICOMPENSA", maxRew)
        state = transition(state, maxAct)

    seq = unfoldState(state, n)
    if(isValid(seq)):
        #print(seq)
        #print("=== Configurazione trovata ===")
        printTertiary(fillMatrix(seq, primary))
        print("=== Energia della configurazione ===", score(fillMatrix(seq, primary), countH(primary)[3]))
