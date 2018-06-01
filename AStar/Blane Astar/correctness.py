import pathfinding
from pathfinding import testfunc
from pathfinding import getneighbors
from pathfinding import retrace
from pathfinding import Node
from pathfinding import GRAPH
from Astar import algo


class Correctness(object):

    def __init__(self):
        self.correctness = 0
        self.pathaccuracy = 0
        self.successrate = 0
        self.complete = False
        self.testlist = []

# ***
def checksuccessrate(t):
    resultlist = []
    returnvalue = 1
    for i in range(len(result)):
        for _ in range(100):
            result = t[i]
            if result:
                resultlist.append(True)
            else:
                result.append(False)
    
    for j in range(len(resultlist)):
        if resultlist[j] == False:
            returnvalue -= len(resultlist) / j
    
    return returnvalue

#   *** rework once other Astar algorithm is made avalible
def setuptests(astartype):
    testlist = []
    if astartype == 1:
        test1 = testfunc(pathfinding.astar(GRAPH[35], GRAPH[65], GRAPH))
        test2 = testfunc(pathfinding.astar(GRAPH[0], GRAPH[99], GRAPH))
        test3 = testfunc(pathfinding.astar(GRAPH[23], GRAPH[56], GRAPH))
        testlist = [test1, test2, test3]
    elif astartype == 2:
        # for second astar algorithm
    
    #successrate is assigned
    successrate = checksuccessrate(testlist)


# *** What's needed:
# Checking path accuracy
# Have setup for ready for path accuracy
# Calculate total correctness
# Cleanup