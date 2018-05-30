from node import Node

class neighbors(object):
    def __init__(self, position, identity):
        self.position = position
        self.identity = identity
        self.parent = None
        self.walkable = True
        self.neighbors = []
        self.gscore = 0
        self.hscore = 0
        self.fscore = 0
    


    def manhattan(start, goal):
        ydiff = abs(goal[1] - start[1])
        xdiff = abs(goal[0] - start[0])
        
        return xdiff + ydiff

    def movementcost(start, goal):
        if start[0] == goal[0] or start[1] == goal[1]:
            return 10
        else:
            return 14

    def getneighbors(node, nodes):
        current = node
        
        top = (current[0], current[1] + 1)
        topright = (current[0] + 1, cuurrent[1] + 1)
        right = (current[0] + 1, current[1])
        bottomright = (current[0] + 1, current[1] - 1)
        bottom = (current[0], current[1] - 1)
        bottomleft = (current[0] - 1, current[1] - 1)
        left = (current[0] - 1, current[1])
        topleft = (current[0] - 1, current[1] - 1)
        
        directions = [top, topright, right, bottomright, bottom, bottomleft, left, topleft]
        neighbors = []

        for i in nodes:
            node = (i[0], i[1])
            if node in directions:
                neighbors.append(i)

        return neighbors