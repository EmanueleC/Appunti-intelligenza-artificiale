from constraint import *

problem = Problem()

problem.addVariable('x', [10,20,30])
problem.addVariable('y', [40,50,16])
problem.addVariable('z', [4,5,6])

problem.addConstraint(lambda a,b: a < b, ('x','y'))
problem.addConstraint(lambda a,b,c: a + b + c < 65, ('x','y','z'))

solutions = problem.getSolutions()
print(solutions)
