from constraint import *
from pfp import *

#primary = "HHPH"

def constraint(primary, half):
    lenProtein = len(primary)

    problem = Problem()

    k = 1

    if(half): k = 2

    # x/y-coordinates for amminoacids
    for i in range(lenProtein):
        problem.addVariable("x" + str(i), range(0,int(lenProtein/k)))
        problem.addVariable("y" + str(i), range(0,int(lenProtein/k)))

    # utility lists
    xPairs = []
    yPairs = []
    xyPairs = []

    for i in range(lenProtein-1):
        xPairs.append(["x" + str(i), "x" + str(i+1)])
        yPairs.append(["y" + str(i), "y" + str(i+1)])

    for i in range(lenProtein):
        for j in range(i):
            xyPairs.append(["x" + str(i), "y" + str(i), "x" + str(j), "y" + str(j)])

    #print(xyPairs)

    # distance between amminoacids
    for i in range(len(xPairs)):
        #print(xPairs[i][0], xPairs[i][1], yPairs[i][0], yPairs[i][1])
        problem.addConstraint(lambda x1, x2, y1, y2: abs(y1 - y2) + abs(x1 - x2) == 1, (xPairs[i][0], xPairs[i][1], yPairs[i][0], yPairs[i][1]))

    for i in range(len(xyPairs)):
        problem.addConstraint(lambda x1, y1, x2, y2: not (x1 == x2 and y1 == y2), (xyPairs[i][0], xyPairs[i][1], xyPairs[i][2], xyPairs[i][3]) )

    solutions = problem.getSolutions()
    return solutions

def adjustSol(sol, n):
    sequence = []
    #print(sol)
    for i in range(0,n):
        pos = sol['x'+str(i)]
        pos = pos + sol['y'+str(i)]*n
        sequence.append(pos)

    return sequence

def generateSeq(primary):
    solutions = constraint(primary, False)
    sequences = []
    for sol in solutions:
        sequence = adjustSol(sol, len(primary))
        sequences.append(sequence)
    return sequences

def breakSymmetries(sequences):
    toBeDeleted = []
    for i in range(len(sequences)):
        for j in range(i):
            if(sorted(sequences[i]) == sorted(sequences[j])):
                toBeDeleted.append(i)
    #print("Lists indexes duplicate: ", toBeDeleted)
    filtered = [x for i, x in enumerate(sequences) if i not in toBeDeleted]
    return filtered

def generateSol(primary):
    print("Constraint problem...")
    sequences = generateSeq(primary)
    #print(sequences)
    print("Before breaking symmetry:", len(sequences))
    sequences2 = breakSymmetries(sequences)
    print("After breaking symmetry:", len(sequences2))
    best = 0
    points = 0
    for sequence in sequences2:
        tertiary = fillMatrix(sequence, primary)
        #printTertiary(tertiary)
        #print(sequence)
        points = score(tertiary, countH(primary)[3])
        if(points > best):
            #print("score:", points)
            best = points
    return best

def test(seq, function):
    start = timeit.default_timer()
    r = function(seq, i)
    stop = timeit.default_timer()
    time = stop - start
    return r, time

test_seq = "HHPH"
easy = "HPHHPHHPH"
medium = "PPHPHPPPPHPHHPHP"
difficult = "HPHPPHHPHPPHPHHPPHPH"
hard = "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP"

test(test_seq, generateSol)
test(easy, generateSol)
test(medium, generateSol)
test(difficult, generateSol)
test(hard, generateSol)
