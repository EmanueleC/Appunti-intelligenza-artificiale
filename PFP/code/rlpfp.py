from pfp import *
from numpy.random import choice
import random
import math

actionSpace = ['L', 'U', 'R', 'D']
actionDict = {'L' : 1, 'U' : 2, 'R' : 3, 'D' : 4}
discountFactor = 0.9
saved = []

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
    #print("da: ", state, "a: ", (state * 4) - 3 + actionDict[action], "con l'azione", action)
    return (state * 4) - 3 + actionDict[action]

""" returns the reward for the pair (state, action) """
def reward(state, n, primary):
    if(not isValid(unfoldState(state, n))):
        #print("Stato non valido, tempo sprecato per unfoldare\dots")
        return 0.01
    elif(isFinal(state, n)):
        #print("Stato finale valido con energia: ", state, energy(unfoldState(state, n), primary))
        en = energy(unfoldState(state, n), primary)
        return en
    else:
        #print("Avanti")
        return 0.1

""" Qf function - returns the current reward and future reward of a given state """
def Qf(state, action, n, discountFactor, Q, primary):
    nextState = transition(state, action)
    currRew = reward(nextState, n, primary)
    futureRew = 0
    for i in actionSpace:
        if (nextState, i) in Q:
            rew = Q[(nextState, i)]
            if(rew > futureRew): futureRew = rew
    #print("futureRew", futureRew)
    total = currRew + (discountFactor * futureRew)
    #print(total)
    return total

def QL(primary, episodes, seed):
    if(seed != -1): random.seed(seed)
    opt = False
    #print(episodes)
    n = len(primary)
    startState = 1
    Q = {}

    #print("TRAINING...")

    for i in range(episodes):
        state = startState
        while(not isFinal(state, n)):
            maxRew = 0
            maxAct = 'L'
            if((state, 'L') in Q): maxRew = Q[(state, 'L')]
            for a in actionSpace:
                rew = -1
                if((state, a) in Q): rew = Q[(state, a)]
                if(rew > maxRew):
                    maxRew = rew
                    maxAct = a
            randomAct = random.choice(actionSpace)
            act = choice([maxAct, randomAct], p = [0, 1])
            rew = Qf(state, act, n, discountFactor, Q, primary)
            if(rew != 0): Q[(state, act)] = rew
            state = transition(state, act)

    '''for i in range(1, 100):
        for a in actionSpace:
            if((i,a) in Q):
                print "%s: %s" % ((i,a), Q[(i,a)])'''

    #print("TEST...")
    
    st = startState
    while(not isFinal(st, n)):
        #print(state)
        maxAct = random.choice(actionSpace)
        if(st, maxAct) in Q: maxRew = Q[(st, maxAct)]
        else: maxRew = 0
        for i in actionSpace:
            rew = 0
            if(st, i) in Q:
                rew = Q[(st, i)]
            if(rew > maxRew):
                maxRew = rew
                maxAct = i
        #print("AZIONE", maxAct, "RICOMPENSA", maxRew)
        st = transition(st, maxAct)

    energy = -1
    tertiary = {}
    seq = {}
    if(isValid(unfoldState(st, n))):  
        seq = unfoldState(st, n)
        tertiary = fillMatrix(seq, primary)
        energy = score(fillMatrix(seq, primary), countH(primary)[3])
        #print(n)
        #print(seq)
        #print("=== Energia della configurazione ===", score(fillMatrix(seq, primary), countH(primary)[3]))
    return energy, tertiary, seq
