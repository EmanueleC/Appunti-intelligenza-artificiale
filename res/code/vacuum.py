import networkx as nx
import matplotlib.pyplot as plt

class State:
    def __init__(self, array):
        self.array = array

    def compare(self,other):
        for i in xrange(1,len(self.array)):
            if(not (self.array[i].compare(other.array[i]))):
                return False
        return True
    
    def getString(self):
		strings = ""
		for i in range(0,len(self.array)-1):
			strings = strings + self.array[i].getString() + ","
		strings = strings + self.array[len(self.array)-1].getString()
		return strings

class Pair:
    def __init__(self, location, prop):
        self.location = location
        self.prop = prop
    
    def suck(self):
        print "Suck"
        self.prop = "Clean"
    
    def compare(self,other):
        if(self.location == other.location and self.prop == other.prop): return True
        else: return False
        
    def getString(self):
        return self.location + " " + self.prop

class Agent:
    def __init__(self, where):
        self.where = where

    def move(self):
        print "Move"
        if (self.where == "A"):
            self.where = "B"
        else:
            self.where = "A"
     
    def start(self, initial, goal):
        while(not initial.compare(goal)):
            for el in initial.array:
                print(initial.getString())
                if (el.prop == "Dirty" and el.location == self.where):
                    el.suck()
                else:
                    self.move()
                    el.suck()
            print(initial.getString())

def graph():
	allClean = State([Pair("A","Clean"),Pair("B","Clean")]).getString()
	allDirty = State([Pair("A","Dirty"),Pair("B","Dirty")]).getString()
	cleanDirty = State([Pair("A","Dirty"),Pair("B","Clean")]).getString()
	dirtyClean = State([Pair("A","Clean"),Pair("B","Dirty")]).getString()
	graph = nx.Graph()
	graph.add_node(allClean)
	graph.add_node(allDirty)
	graph.add_node(cleanDirty)
	graph.add_node(dirtyClean)
	graph.add_edge(allClean,cleanDirty)
	graph.add_edge(allClean,dirtyClean)
	graph.add_edge(allDirty,cleanDirty)
	graph.add_edge(allDirty,dirtyClean)
	return graph

vacuum = Agent("A")
pair1 = Pair("A","Dirty")
pair2 = Pair("B","Dirty")
array = [pair1,pair2]
pairGoal1 = Pair("A","Clean")
pairGoal2 = Pair("B","Clean")
arrayGoal = [pairGoal1,pairGoal2]
initialState = State(array)
goalState = State(arrayGoal)
vacuum.start(initialState,goalState)
g = graph()
pos = nx.spring_layout(g)
nx.draw(g,pos=pos,with_labels=True)
plt.savefig("vacummTree.png")
