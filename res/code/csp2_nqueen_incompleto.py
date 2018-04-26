from constraint import *

def stampaSol(soluzione):
	n=len(soluzione)
	
	for rows in range(n):
		s=""
		for cols in range(n):
			if n-rows-1 == soluzione[cols]:
				s += "Q"
			else:
				s += "-"
		

		print(s)

n=5

problem = Problem()

for i in range(n):
	problem.addVariable(i, range(n))

#########################################################
'''
Modellare di seguito il vincolo delle diagonali
'''

for i in range(n):
    for j in range(i+1,n):
        problem.addConstraint(lambda a,b, i=i, j=j: a - b != i - j, (i,j))

for i in range(n):
    for j in range(i+1,n):
        problem.addConstraint(lambda a,b, i=i, j=j: a - b != j - i, (i,j))


#########################################################	
problem.addConstraint(AllDifferentConstraint())


solutions = problem.getSolution()
print(solutions)
stampaSol(solutions)
