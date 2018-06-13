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


blane_graph = []
counter = 0
for ypos in range(10):
    for xpos in range(10):
        blane_graph.append(Node(counter, (xpos, ypos)))
        counter += 1

def retrace(goal):
    current = goal
    path = []
    while current:
        path.append(current)
        current = current.parent
    return path

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


def blane_astar(start, goal, graph):
    current = start
    openlist = [current]
    closedlist = []
    path = []
    #   bad stuff that brings the wrong result 
    return path