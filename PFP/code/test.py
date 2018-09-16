from pfp import *
from rlpfp import *
import random
import math
import timeit
import sys

sys.stdout=open("test.txt","w")

# sample proteins
test_seq = "HHPH"
easy = "HPHHPHHPH"
medium = "PPHPHPPPPHPHHPHP"
difficult = "HPHPPHHPHPPHPHHPPHPH"
hard = "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP"

def test(seq, function, i, seed):
    start = timeit.default_timer()
    r = function(seq, i, seed)
    stop = timeit.default_timer()
    time = stop - start
    return r, time

def findBest(seq, function, maxIt, seed):
    m = -1
    t = -1
    it = -1
    for i in range(maxIt):
        r, time = test(seq, function, i, seed)
        if(r > m):
            m = r
            t = time
            it = i
    print(str(function) + " " + str(seq), "energy: " + str(m), "time: " + str(t), "iterations: " + str(it), "seed: " + str(seed))

seeds = {3, 1234, 42, -1}

for seed in seeds:

    exLS = False

    print("==============================")

    if(exLS):

        findBest(test_seq, LS, 20, seed)
        findBest(easy, LS, 30, seed)
        findBest(medium, LS, 50, seed)
        findBest(difficult, LS, 70, seed)
        findBest(hard, LS, 150, seed)

        print("==============================")
    
    findBest(test_seq, QL, 50, seed)
    #findBest(easy, QL, 150, seed)
    #findBest(medium, QL, 250, seed)
    #findBest(difficult, QL, 500, seed)
    #findBest(hard, QL, 1000, seed)

sys.stdout.close()
