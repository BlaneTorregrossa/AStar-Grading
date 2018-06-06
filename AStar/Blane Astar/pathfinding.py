import math


class Node(object):


    def __init__(self, guid, position):
        
        self.guid = ''
        if guid < 10:
            self.guid = str('0' + str(guid))
        else:
            self.guid = str(guid)

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
        return str.format('({0}) ', self.guid)

def manhattan(start, goal):
    ydif = abs(goal[1] - start[1])
    xdif = abs(goal[0] - start[0])

    return xdif + ydif


def costtomove(start, goal):
    if start[0] == goal[0] or start[1] == goal[1]:
        return 10
    return 14


def getneighbors(node, nodes):
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
            if node in closedlist:
                pass
            node.h = manhattan(node, goal)
            node.f = node.g + node.h
        current = openlist[0]
    for node in range(0, len(openlist)):
        for nodecmp in range(0, len(openlist)):
            if openlist[node].fscore < openlist[nodecmp].fscore:
                temp = openlist[nodecmp]
                openlist[nodecmp] = openlist[node]
                openlist[node] = temp
    return path






