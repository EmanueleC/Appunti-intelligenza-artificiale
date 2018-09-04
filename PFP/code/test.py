from pfp import *
from rlpfp import *
from constraints import *
import random
import math
import timeit

primary = "PPHPHPPPPHPHHPHP"

start = timeit.default_timer()
generateSol(primary)
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
LS(primary)
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
QL(primary)
stop = timeit.default_timer()
print('Time: ', stop - start)
