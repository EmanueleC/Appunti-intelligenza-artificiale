from pfp import *
from rlpfp import *
import random
import math
import timeit
import sys

# sample proteins
test_seq = "HHPH"
easy = "HPHHPHHPH"
medium = "PPHPHPPPPHPHHPHP"
difficult = "HPHPPHHPHPPHPHHPPHPH"
hard = "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP"

def test(seq, function, i, seed):
    start = timeit.default_timer()
    r, st, act = function(seq, i, seed)
    stop = timeit.default_timer()
    time = stop - start
    return r, st, act, time

def findBest(seq, function, startIt, maxIt, seed):
    m = -1
    t = -1
    it = -1
    bSt = {}
    bAct = {}
    for i in range(startIt, maxIt):
        #print(i)
        r, st, act, time = test(seq, function, i, seed)
        if(r >= m and act != []):
            m = r
            t = time
            it = i
            bSt = st
            bAct = act
            #print(str(function) + " " + str(seq), bAct)
            #printTertiary(bSt)
            print(str(function) + " " + str(test), "energy: " + str(m), "time: " + str(t), "iterations: " + str(it), "seed: " + str(seed))

seeds = {3, 42, 1234, -1}

for seed in seeds:

    exLS = False
    print("==============================")

    if(exLS):
        findBest(test_seq, LS, 0, 50, seed)
        findBest(easy, LS, 0, 200, seed)
        findBest(medium, LS, 0, 500, seed)
        findBest(difficult, LS, 0, 1000, seed)
        findBest(hard, LS, 0, 2000, seed)
        print("==============================")

    findBest(test_seq, QL, 0, 200, seed)
    findBest(easy, QL, 0, 200, seed)
    findBest(medium, QL, 0, 500, seed)
    findBest(difficult, QL, 0, 1000, seed)
    findBest(hard, QL, 0, 2000, seed)
