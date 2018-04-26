from constraint import *
import networkx as nx
import matplotlib.pyplot as plt

problem = Problem()

problem.addVariables(['WA','NT','Q','NSW','V','SA','T'],['r','g','b'])

problem.addConstraint(lambda a,b: a != b, ('WA','SA'))
problem.addConstraint(lambda a,b: a != b, ('WA','NT'))
problem.addConstraint(lambda a,b: a != b, ('NT','SA'))
problem.addConstraint(lambda a,b: a != b, ('NT','Q'))
problem.addConstraint(lambda a,b: a != b, ('Q','SA'))
problem.addConstraint(lambda a,b: a != b, ('Q','NSW'))
problem.addConstraint(lambda a,b: a != b, ('NSW','SA'))
problem.addConstraint(lambda a,b: a != b, ('NSW','V'))
problem.addConstraint(lambda a,b: a != b, ('V','SA'))

node_list = ['WA','NT','Q','NSW','V','SA','T']

solutions = problem.getSolutions()
print(solutions)

graph=nx.Graph()

for i in node_list:
    graph.add_node(i)

graph.add_edge("SA","WA")
graph.add_edge("SA","NT")
graph.add_edge("SA","Q")
graph.add_edge("SA","NSW")
graph.add_edge("SA","V")
graph.add_edge("NT","WA")
graph.add_edge("NT","Q")
graph.add_edge("Q","NSW")
graph.add_edge("V","NSW")

pos = nx.spring_layout(graph)
nx.draw(graph,pos=pos,with_labels=True)
for i in range(0,7):
 nx.draw_networkx_nodes(graph,pos=pos,nodelist=[node_list[i]],node_color = solutions[0].get(node_list[i]),width=5)
plt.savefig("australia.png")
