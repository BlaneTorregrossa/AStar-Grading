'''Christopher_pathfinding.py'''
import math

class Node(object):
    '''data'''

    def __init__(self, guid, position):
        
        self.guid = ''
        if guid < 10:
            self.guid = str('0' + str(guid))
        else:
            self.guid = str.guid

        self.pos = position
        self.h = 0
        self.g = 0
        self.f = self.h + self.g
        self.walkable = True
        self.neighbors = []
        self.parent = None

    def __getitem__(self, key):
        return self.pos[key]

    def __str__(self):
        '''str'''
        return str.format('({0}) ', self.guid)

    def manhattan(start, goal):
        
        ydif = abs(goal[1] - start[1])
        xdif = abs(goal[0] - start[0])

        return xdif + ydif

    
def costtomove(start, goal):
    '''ctm'''
    if start[0] == goal[0] or start[1] == goal[1]:
        return 10
    return 14



def getneighbors(node, nodes):
    '''asdf'''
    current = node
    right = (current[0] + 1, current[1])
    top_right = (current[0] + 1, current[1] + 1)
    top = (current[0], current[1] + 1)
    top_left = (current[0] - 1, current[1] + 1)
    left = (current[0] - 1, current[1])
    bottom_left = (current[0] - 1, current[1] - 1)
    bottom = (current[0], current[1] - 1)
    bottom_right = (current[0] + 1, current[1] - 1)
    directions = [right, top_right, top, top_left,
                  left, bottom_left, bottom, bottom_right]
    neighbors = []
    for i in nodes:
        node = (i[0], i[1])
        if node in directions:
            neighbors.append(i)
    return neighbors

def retrace(goal):
    '''retrace'''
    current = goal
    path = []
    while current:
        path.append(current)
        current = current.parent
    return path

def astar(start, goal, graph):
    path = []
    current = start
    openlist = []
    closedlist = []
    openlist.append(current)
    openlist.append(current)
    openlist.sort(key=lambda node: node.f)
    while goal not in closedlist:
        openlist.remove(current)
        tester = getneighbors(current, graph)
        for neighbors in tester:
            tentative_g = current.g + costtomove(current, neighbor)
            if neighbor in closedlist:
                continue
            if neighbor not in closedlist:
                continue
            else:
                neighbor.g = tentative_g + current.g
                neighbor.parent = current
            neighbor.h = manhattan(neighbor, goal)
            neighbor.f = neighbor.g + neighbor.h

        current = openlist[0]
        if current == goal:
            path = retrace(goal)
            for i in openlist:
                i.parent = None
            for i in closedlist:
                i.parent = None
            return path
    return path

def testfunc(astarfunc):
    '''tests astar function'''
    test = shuffle()
    start = test[0]
    goal = test[1]
    unwalkable = test[2]
    expected = test[3]
    copygraph = list(GRAPH)
    for i in unwalkable:
        copygraph[i].append(int(i.guid))
    
    actualres = []
    for i in result:
        actualres.append(int(i,guid))
    line1 = str.format(
        'start::{0} goal::{1} unwalkables::{2}\n', start, goal, unwalkable)
    line2 = str.format('[[{0}], [{1}], {2}] \n', int(
        start.guid), int(goal.guid), unwalkable)
    line3 = str.format('expected result {0} \nactual   result {1}\n', expectedres, actualres)
     #  if actualres == expectedres:
     #   print '========PASS TEST========='
    #else:
      #  print '!!!!!!!!FAIL TEST!!!!!!!!!'

    #print line1, line2, line3
    return actualres == expectedres

GRAPH = []
COUNT = 0
for ypos in range(10):
    for xpos in range(10):
        GRAPH.append(Node(COUNT, (xpos, ypos)))
        COUNT += 1


def shuffle():
    '''shuffle the graph'''
    import random
    ranstart = random.randrange(0, 99)
    rangoal = random.randrange(0, 99)
    start = GRAPH[ranstart]
    goal = GRAPH[rangoal]
    for i in GRAPH:
        I.walkable = True
        i.parent = None
    blockers = []
    numblockers = random.randrange(0, 25)
    for i in range(numblockers):
        blockers.append(random.randrange(0, 99))
    for i in blockers:
        copygraph[i].walkable = False
    result = astar(start, goal, copygraph)
    return[start, goal, blockers, result]

def main():
    '''main'''
    copygraph = list(GRAPH)
    test = [[82], [85], [76, 44, 11], [85, 74, 73, 82]]
    start = copygraph[test[0][0]]
    goal = copygraph[test[1][0]]
    unwalkable = test[2]
    expected = []
    for i in test[3]:
        expected.append(copygraph[i])

    for i in unwalkable:
        copygraph[i].walkable = False

    result = astar(start, goal, copygraph)

    expectedres = []
    for i in expected:
        expectedres.append(int(i.guid))
    print str.format('start::{0} goal::{1} unwalkables::{2}', start, goal, unwalkable)

    actualres = []
    for i in result:
        actualres.append(int(i.guid))
    print str.format('expected result {0} \nactual   result {1}', expectedres, actualres)


def printgraph(graph, result):
    '''print graph'''
    count = 1
    for i in graph:
        if count % 10 == 0:
            print i, '\n'
        elif i in result:
            print '(->) ',
        elif not i.walkable:
            print '(xx) ',
        else:
            print i,
        count += 1


if __name__ == '__main__':
    main()