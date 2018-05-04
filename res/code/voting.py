from constraint import *
import networkx as nx
import matplotlib.pyplot as plt

file_handle = open('voti.txt')

candidati = []

for i in range(12):
    candidati.append(0)

approval = 1
copeland = True

for line in file_handle:
    i = 0
    count = 0
    for x in line.split(','):
        if (i < approval and not copeland):
            candidati[int(x)-1] = candidati[int(x)-1] - 1
        elif (copeland):
            candidati[int(x)-1] = candidati[int(x)-1] + count - 1
        else: break
        count = count + 1
    i = i + 1

candidatiWon = {}
for i in range(len(candidati)):
    candidatiWon[i] = []

counti = 0
for i in candidati:
    countj = 0
    for j in candidati:
        if(countj != counti and candidati[counti] > candidati[countj]):
            candidatiWon[counti].append(countj)
        countj = countj + 1
    counti = counti + 1

print(candidati)
print(candidatiWon)

graph=nx.DiGraph()

for i in range(len(candidati)):
    graph.add_node(i)

for i in candidatiWon:
    for j in candidatiWon[i]:
        graph.add_edges_from([(i,j)])

pos = nx.spring_layout(graph)
nx.draw(graph,pos=pos,with_labels=True)
plt.savefig("voting.png")
