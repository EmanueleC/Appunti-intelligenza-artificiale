from pfp import *
from rlpfp import *
#from constraints import *
import random
import math
import timeit

# sample proteins
easy = "HPHHPHHPH"
medium = "PPHPHPPPPHPHHPHP"
difficult = "HPHPPHHPHPPHPHHPPHPH"
hard = "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP"

def test(test, function):
    start = timeit.default_timer()
    function(test)
    stop = timeit.default_timer()
    print('Time: ', stop - start)


test(easy,LS)
test(easy,QL)
test(medium,LS)
test(medium,QL)
test(difficult,LS)
test(difficult,QL)
test(hard,LS)
test(hard,QL)

