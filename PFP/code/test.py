from pfp import *
from rlpfp import *
import random
import math
import timeit
import sys

sys.stdout = open("LSHardVariousIt.txt","w")

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
        if(r > m and act != []):
            m = r
            t = time
            it = i
            bSt = st
            bAct = act
            print(str(function) + " " + str(seq), bAct)
            printTertiary(bSt)
            print(str(function) + " " + str(seq), "energy: " + str(m), "time: " + str(t), "iterations: " + str(it), "seed: " + str(seed))

seeds = {3, 42, 1234, -1}
its = {500, 1000, 1200, 1500, 1600, 1700, 1800, 2000, 2500, 2700, 3000, 3200, 3500, 4000, 4500, 5000, 5500, 6000}
for seed in seeds:
    for it in its:
        r, st, act, time = test(hard, LS, it, seed)
        print(str(LS) + " " + str(hard), act)
        printTertiary(st)
        print(str(LS) + " " + str(hard), "energy: " + str(r), "time: " + str(time), "seed: " + str(seed), "it: " + str(it))

    '''exLS = False
    print("==============================")

    if(exLS):
        #findBest(test_seq, LS, 50, seed)
        #findBest(easy, LS, 200, seed)
        #findBest(medium, LS, 500, seed)
        #findBest(difficult, LS, 1000, seed)
        #findBest(hard, LS, 0, 500, seed)
        print("==============================")

    #findBest(test_seq, QL, 0, 200, seed)
    #findBest(easy, QL, 0, 200, seed)
    #findBest(medium, QL, 100, 500, seed)
    #findBest(difficult, QL, 1000, seed)
    findBest(hard, QL, 1500, 2000, seed)'''

# 50, 200, 500, 1000, 2000

sys.stdout.close()
