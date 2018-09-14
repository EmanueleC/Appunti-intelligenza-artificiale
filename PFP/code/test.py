from pfp import *
from rlpfp import *
import random
import math
import timeit

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

#primo terminale opt false
#secondo terminale true

    exLS = True

    print("==============================")

    if(exLS):

        #findBest(test_seq, LS, 250, seed)
        findBest(easy, LS, 500, seed)
        #findBest(medium, LS, 1000, seed)
        #findBest(difficult, LS, 3000, seed)
        #findBest(hard, LS, 5000, seed)

    print("==============================")

    #findBest(test_seq, QL, 250, seed)
    #findBest(easy, QL, 500, seed)
    #findBest(medium, QL, 1000, seed)
    #findBest(difficult, QL, 3000, seed)
    #findBest(hard, QL, 5000, seed)
