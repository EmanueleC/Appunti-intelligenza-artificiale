class State:
    def __init__(self, array):
        self.array = array

    def compare(self,other):
        for i in xrange(1,len(self.array)):
            if(not (self.array[i].compare(other.array[i]))):
                return False
        return True
    
    def getString(self):
        for el in self.array:
            el.getString()

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
        print self.location + " " + self.prop

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
                initial.getString()
                if (el.prop == "Dirty" and el.location == self.where):
                    el.suck()
                else:
                    self.move()
                    el.suck()
            initial.getString()

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