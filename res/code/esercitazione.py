import networkx as nx
import matplotlib.pyplot as plt

def romania():

	node_list = ["Bucharest","Giurgiu","Urziceni","Hirsova","Eforie","Neamt","Oradea","Zerind","Arad","Timisoara","Lugoj","Mehadia","Dobreta","Craiova","Sibiu","Fagaras","Pitesti","Rimnicu Vilcea","Vaslui","Iasi"]

	graph=nx.Graph()

	for i in node_list:
		graph.add_node(i, percorso=[], visitato=False, f=0)

	graph.add_edge("Arad","Zerind", weight=75)
	graph.add_edge("Arad","Timisoara", weight=118)
	graph.add_edge("Arad","Sibiu", weight=140)
	graph.add_edge("Zerind","Oradea", weight=71)
	graph.add_edge("Mehadia","Lugoj", weight=70)
	graph.add_edge("Mehadia","Dobreta", weight=75)
	graph.add_edge("Craiova","Dobreta", weight=120)
	graph.add_edge("Craiova","Rimnicu Vilcea", weight=146)
	graph.add_edge("Craiova","Pitesti", weight=138)
	graph.add_edge("Pitesti","Rimnicu Vilcea", weight=97)
	graph.add_edge("Pitesti","Bucharest", weight=101)
	graph.add_edge("Timisoara","Lugoj", weight=111)
	graph.add_edge("Sibiu","Fagaras", weight=99)
	graph.add_edge("Bucharest","Fagaras", weight=211)
	graph.add_edge("Bucharest","Giurgiu", weight=90)
	graph.add_edge("Bucharest","Urziceni", weight=85)
	graph.add_edge("Vaslui","Urziceni", weight=142)
	graph.add_edge("Vaslui","Iasi", weight=92)
	graph.add_edge("Neamt","Iasi", weight=87)
	graph.add_edge("Hirsova","Urziceni", weight=98)
	graph.add_edge("Hirsova","Eforie", weight=86)
	graph.add_edge("Sibiu","Rimnicu Vilcea", weight=80)
	graph.add_edge("Sibiu","Oradea", weight=151)

	return graph


def h1():

	dict={}
	# i valori rappresentano la distanza della citta da Bucarest
	dict["Bucharest"] = 0
	dict["Giurgiu"] =77
	dict["Urziceni"] = 80
	dict["Hirsova"] = 151
	dict["Eforie"] = 161
	dict["Neamt"] = 234
	dict["Oradea"] = 380
	dict["Zerind"] = 374
	dict["Arad"] = 366
	dict["Timisoara"] = 329
	dict["Lugoj"] = 244
	dict["Mehadia"] = 241
	dict["Dobreta"] = 242
	dict["Craiova"] = 160
	dict["Sibiu"] = 253
	dict["Fagaras"] = 176
	dict["Pitesti"] = 100
	dict["Rimnicu Vilcea"] = 193
	dict["Vaslui"] = 199
	dict["Iasi"] = 226

	return dict

def bfs_paths(graph, start, goal):
	queue = [(start, [start])]
	g.node[start]["percorso"] = g.node[start]["percorso"] + [start]
	while queue:
		(vertex, path) = queue.pop(0)
		if (g.node[vertex]["visitato"] == False):
			g.node[vertex]["visitato"] = True
			for next in g.neighbors(vertex):
				if (g.node[next]["visitato"] == False):
					g.node[next]["f"] = g.node[vertex]["f"] + g.get_edge_data(vertex,next)["weight"]
					g.node[next]["percorso"] = path + [next]
					queue.append((next, path + [next]))
				if(next == goal):
					return path + [next]

def draw_plot(g,goal,color):
	pos = nx.spring_layout(g)
	nx.draw(g,pos=pos,with_labels=True)
	edgelist = []
	for i in range(0,len(g.node[goal]["percorso"])-1):
		edgelist = edgelist + [(g.node[goal]["percorso"][i],g.node[goal]["percorso"][i+1])]
	nodelist = g.node[goal]["percorso"]
	nx.draw_networkx_edges(g,pos=pos,edgelist=edgelist,edge_color = color,width=5)
	nx.draw_networkx_nodes(g,pos=pos,nodelist=nodelist,node_color = color,width=5)
	plt.savefig("path.png")

g = romania()
goal = "Neamt"
start = "Arad"
bfs_paths(g,start,goal)
draw_plot(g,goal,'b')
