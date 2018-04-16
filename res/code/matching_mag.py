import networkx as nx
import matplotlib.pyplot as plt
import random as rnd

graph = nx.Graph()

men_list = ["Mario","Luigi","Carlo","Paolo"]
wives_list = ["UniPD","UniTS","UniMi","UniVe"]

color_map={0:"#0000ff", 1:"#ff0000"}
colors =[]
pos = {}

for m in men_list:
	graph.add_node(m, gender=0, free=True)
	pos[m] = (men_list.index(m), 2)

for w in wives_list:
	graph.add_node(w, gender=1, free=True)
	pos[w] = (wives_list.index(w), 1)
	
colors = [color_map[graph.node[node]['gender']] for node in graph]
	
for m in men_list:
    for w in wives_list:
        graph.add_edge(m,w, weight=int(rnd.uniform(0,1)*10))


G2 = nx.Graph()

############################## TROVA UN MATCHING OTTIMO###############

M = {}
waiting_list = men_list
print(waiting_list)
while (waiting_list != []):
    man = waiting_list.pop(0)
    max_pref = -1;
    for w in wives_list:
        pref = graph[man][w]["weight"]
        if (pref > max_pref):
            max_pref = pref
            woman_pref = w
    graph[man][woman_pref]["weight"] = -1
    if (not (woman_pref in M)):
        M[woman_pref] = man
        print(man, "and", woman_pref, "became engaged")
    else:
        if (graph[man][woman_pref]["weight"] > graph[M[woman_pref]][woman_pref]["weight"]):
            waiting_list = waiting_list + [M[woman_pref]]
            print(M[woman_pref] + "now is free")
            M[woman_pref] = man
        else:
            waiting_list = waiting_list + [man]
            print(man, "still unengaged, he needs to propose to another woman")
    print(waiting_list)

print(M)

######################################################################
for w in wives_list:
   G2.add_edge(M[w],w)

labels = nx.get_edge_attributes(graph,'weight')		
nx.draw(graph, pos, node_color=colors, with_labels=True)
nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels, label_pos=0.3)
nx.draw_networkx_edges(G2,pos,alpha=0.4,edge_color='r',width=10, with_labels=True, edge_labels=labels)
plt.show()
