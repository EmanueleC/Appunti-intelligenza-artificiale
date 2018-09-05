import random

""" calculates an upper bound for H-contacts, counts odd and even contacts and consectutive H pairs in primary structure """
def countH(primary):
    countEven = 0
    countOdd = 0
    count = 0
    countConsH = 0
    prev = False
    for i in range(len(primary)):
        if(primary[i] == 'H'):
            if(prev == True):
                countConsH = countConsH + 1
            prev = True
            if(i % 2 == 0):
                countEven = countEven + 1
            else:
                countOdd = countOdd + 1
        else:
            prev = False
    return [countEven + countOdd, countEven, countOdd, countConsH]

""" print utility function
 example h-h-p
         |
         h-p-h """
def printTertiary(tertiary):
    print("--- tertiary structure ---")
    for i in range(len(tertiary)):
        for j in range(len(tertiary[i])):
            print tertiary[i][j],
        print 
    print("---")

""" fills a 2D square lattice with primary structure (example: [h,h,p,h,p...]), given a sequence guide of numbers """
def fillMatrix(sequence, primary):
    # print('fillMatrix', sequence)
    n = len(primary)
    matrix = [[' ' for i in range(n)] for i in range(n)]
    for i in range(n):
        #print('i_sequence',sequence[i],'i_primary',primary[i])
        matrix[int(sequence[i]/n)][sequence[i] % n] = primary[i]
    return matrix

""" returns a sequence of random numbers compatible with 2D square lattices """
def compose(sequence, n, move):
    directions = []
    if(not move):
        sequence = []
        sequence.append(random.randint(0,(n*n) - 1))
    for i in range(abs(len(sequence)-1), n-1):
        # print('compose start ==>', sequence)
        right = sequence[i] + 1
        left = sequence[i] - 1
        up = sequence[i] - n
        down = sequence[i] + n
        # print('down in sequence', down, down in sequence)
        # print('up in sequence', up, up in sequence)
        choices = {0: up, 1: down, 2: right, 3: left}
        allowed = []
        if(sequence[i] > n-1 and not (up in sequence)):
            allowed.append(0)
        if(sequence[i] < ((n*n) - 1 - n) and not (down in sequence)):
            allowed.append(1)
        if(sequence[i] % n < n-1 and not (right in sequence)):
            allowed.append(2)
        if(sequence[i] % n > 0 and not (left in sequence)):
            allowed.append(3)
        if(allowed == []):
            return -1
        # print('allowed', allowed)
        randomChoice = random.choice(allowed)
        directions.append(randomChoice)
        # print('direction',randomChoice)
        sequence.append(choices.get(randomChoice))
    # print('compose end ==>', sequence)
    return sequence

""" returns the score of a solution """
def score(tertiary, diff):
    score = 0
    n = len(tertiary)
    for i in range(n):
        n_i = len(tertiary[i])
        for j in range(n_i):
            if(tertiary[i][j] == 'H'):
                if(j < n_i -1):
                    if(tertiary[i][j+1] == 'H'): score = score + 1
                if(j > 0):
                    if(tertiary[i][j-1] == 'H'): score = score + 1
                if(i < n-1):
                    if(tertiary[i+1][j] == 'H'): score = score + 1
                if(i > 0):
                    if(tertiary[i-1][j] == 'H'): score = score + 1
    return int(score/2) - diff

""" generates the solution space """
def move(solution):
    n = len(solution)
    cut = random.randint(1,n-1)
    # print('cut at', cut)
    sequence = compose(solution[:cut], n, True)
    while(sequence == -1):
        sequence = compose(solution[:cut], n, True)
    return sequence

""" Local Search """
def LS(primary):
    n = len(primary)
    best = 0
    currBest = 0
    currBestStructure = []
    bestStructure = []
    maxContacts = (min (countH(primary)[1], countH(primary)[2])*2) + 2

    #print("UB per il massimo numero di contatti: ", maxContacts)

    """ combination of random walk and local search """
    for i in range(1000):
        sequence = compose([], n, False)
        # print('initial sequence:', sequence)
        if(sequence != -1):
            solution = fillMatrix(sequence, primary)
            currValue = score(solution, countH(primary)[3])
            oldValue = 0
            while(True):
                newSequence = move(sequence)
                sequence = newSequence
                neighbor = fillMatrix(newSequence, primary)
                oldValue = currValue
                currValue = score(neighbor, countH(primary)[3])
                if(oldValue >= currValue):
                    currBest = currValue
                    currBestStructure = neighbor
                    break
                #else:
                    #print('Score', currValue)
                    #printTertiary(neighbor)
        if(currBest>best):
            #printTertiary(bestStructure)
            best = currBest
            bestStructure = currBestStructure
            #print("Best:", best, "Difference with UB max:", maxContacts - best)
    printTertiary(bestStructure)
    print("=== Energia della configurazione ===", best)

