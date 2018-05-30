import math
import random

class Node(object):
    def __init__(self, guid, position):
        self.guid = ''
        if guid < 10:
            self.guid = str('0' + str(guid))
        else:
            self.guid = str(guid)

        self.pos = positionself.h = 0
        self.h = 0
        self.g = 0
        self.f = self.f = self.h + self.g
        self.walkable = True
        self.neighbors = []
        self.parent = None

    def __getitem__(self, key):
        return self.pos[key]

    def __getstring__(self):
        return str.format('({0})', self.guid)
        
GRAPH = []
COUNT = 0
for ypos in range(10):
    for xpos in range(10):
        GRAPH.append(Node(COUNT, (xpos, ypos)))
        COUNT += 1

def manhattan(start, goal):
    
    ydiff = abs(goal[1]) - start[1])
    xdiff = abs(goal[0] - start[0])
    return xdiff + ydiff

def movementcost(start, goal):
    if start[0] == goal[0] or start[1] == goal[1]:
        return 10
    else:
        return 14

def getneighbors(node, nodes):
    current = node
    right = (current[0] + 1, current[1])
    topright = (current[0] + 1, current[1] + 1)
    top = (current[0], current[1] + 1)
    topleft = (current[0] - 1, current[1] + 1)
    left = (current[0] - 1, current[1])
    bottomleft = (current[0] - 1, current[1] - 1)
    bottom = (current[0], current[1] - 1)
    bottomright = (current[0] + 1, current[1] - 1)
    directions = [right, topright, top, topleft, left,
                    bottomleft, bottom, bottomright]
    neighbors = []

    for i in nodes:
        node = (i[0], i[1])
        if node in directions:
            neighbors.append(i)

    return neighbors

def retracepath(goal):
    current = goal
    path = []

    while current:
        path.append(current)
        current = current.parent

    return path

def astar(start, goal, graph):
    current = start
    openlist = [current]
    closedlist = []
    path = []

    while openlist:
        openlist.remove(current)
        closedlist.append(start)
       
        for node in getneighbors(current, graph):
            if node not in openlist and node not in closedlist:
                openlist.append(node)
            node.g = costtomove(current, node) + current.g
            tentative_g = node.g
            # if node in closedlist:
            node.h = manhattan(node, goal)
            node.f = node.g + node.h
        current = openlist[0]
    
    for node in range(0, len(openlist)):
        for nodealt in range(0, len(openlist)):
            if openlist[node].fscore < openlist[nodealt].fscore:
                temp = openlist[nodealt]
                openlist[nodealt] = openlist[node]
                openlist[node] = temp

    return path

def shuffle():
    rangestart = random.randrange(0, 99)
    rangegoal = random.randrange(0,99)
    start = GRAPH[rangestart]
    goal = GRAPH[rangegoal]
    for i in GRAPH:
        i.walkable = True
        i.parent = None
    blockers = []
    numblockers = random.randrange(0, 25)
    for i in range(numblockers):
        blockers.append(random.randrange(0, 99))
    copygraph = list(GRAPH)
    for i in blcokers:
        copygraph[i].walkable = False
    result = astar(start, goal, copygraph)
    return [start, goal, blockers, result]
    

# def testrun(currentfunction):
#     test = shuffle()
#     start = test[0]
#     goal = test[1]
#     unwalkable = test[2]
#     expected = test[3]
#     copygraph = list(GRAPH)
#     for i in unwalkable:
#         copygraph[i].walkable = False
    
#     result = currentfunction(start, goal, copygraph)

#     expectedresult = []
#     for i in expected:
#         expectedresult.append(int(i.guid))

#     givenresult = []
#     for i in result:
#         givenresult.append(int(i.guid))
    
#     line1 = str.format('start::{0} goal::{1} unwalkables::{2}\n', start, goal, unwalkable)
#     line2 = str.format('[[{0}], [{1}], {2}] \n', int(start.guid), int(goal.guid), unwalkable)
#     line3 = str.format('expected result {0} \n given result {1}\n', expectedresult, givenresult)

#     givenresult = expectedresult
#     return givenresult


def main():
    copygraph = list(GRAPH)
    test = []
    start = copygraph[test[0][0]]
    goal = copygraph[test[1][0]]
    unwalkable = test[2]
    expected = []
    for i in test[3]:
        expected.append(copygraph[i])
    
    for i in unwalkable:
        copygraph[i].walkable = False

    result = astar(start, goal, copygraph)

    expectedresult = []
    for i in expected:
        expected.append(int(i.guid))
    print str.format('start::{0} goal::{1} unwalkables::{2}\n', start, goal, unwalkable)
    
    givenresult = []
    for i in result:
        givenresult.append(int(i.guid))
    print str.format('expected result {0} \n given result {1}\n', expectedresult, givenresult)
    

def printgraph(graph, result):
    count = 1
    for i in graph:
        if count % 10 == 0:
            print i, '\n'
        elif i in result:
            print'(->) ',
        elif not i.walkable:
            print '(X) ',
        else:
            print i,
        count += 1




if __name__ == '__main__':
    main()