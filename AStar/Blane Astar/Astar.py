import node
import graph
from node import Node       #imports Node class from node.py
from graph import Graph     #imports Graph class from graph.py
import pathfinding

class AStar(object):
    def __init__(self, start, goal, graph):
        self.start = start
        self.goal = goal
        self.graph = graph
        self.current = start
        self.openlist = [self.current]
        self.closedlist = [] 
        self.parentlist = []

def getnode(self, identity, graph):
    for node in graph.nodes:
        if node.identity == identity:
            return node

# Collects neighbors from adjacent areas to the given node on the given graph
def test_neighbors(self, node, graph):
    neighbors = []
    left = [node.position[0] - 1, node.position[1]]
    bottom = [node.position[0], node.position[1] - 1]
    right = [node.position[0] + 1, node.position[1]]
    top = [node.position[0], node.position[1] + 1]
    top_left = [node.position[0] - 1, node.position[1] + 1]
    bottom_left = [node.position[0] - 1, node.position[1] - 1]
    top_right = [node.position[0] + 1, node.position[1] + 1]
    bottom_right = [node.position[0] + 1, node.position[1] - 1]
    validposition = [left, bottom, right, top, top_left, bottom_left, top_right, bottom_right]

    for graphnode in graph.nodes:
        for position in validposition:
            if graphnode.position[0] == position[0] and graphnode.position[1] == position[1]:
                if graphnode.walkable:
                    neighbors.append(graphnode)

    return neighbors


def algo(self, start, goal, graph):
    current = start
    openlist = [current]
    closedlist = []
    path = []
    while openlist:
        openlist.remove(current)
        closedlist.append(start)
        for node in pathfinding.getneighbors(current, graph):            
            if node not in openlist and node not in closedlist:
                openlist.append(node)
            node.calculategscore(current)
            node.calculatehscore(goal)
            node.calculatefscore()
        current = openlist[0]
    for node in range(0, len(openlist)):
        for nodecmp in range(0, len(openlist)):
            if openlist[node].fscore < openlist[nodecmp].fscore:
                temp = openlist[nodecmp]
                openlist[nodecmp] = openlist[node]
                openlist[node] = temp

def retraceparents(self):
    self.parentlist.append(self.goal)
    recentparent = self.goal
    recentparent.path = True
    while recentparent != self.start:
        self.parentlist.append(recentparent.parent)
        recentparent = recentparent.parent
        recentparent.path = True


