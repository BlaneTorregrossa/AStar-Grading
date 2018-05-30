from node import Node

# Class for graph which contains the space which astar is to use
class Graph(object):
    def __init__(self):
        self.graph = [] # empty array for graph
        self.counter = 0    #   Counter at starting value (0)

    #   To generate a graph for to hold nodes in a 2d Array 
    #   double for loop which generates the graph row by row
    #   has a counter to keep track of current position
    def generategraph(self, length, height):
        for ypos in range(height):
            for xpos in range(length):
                self.graph.append(Node(self.counter, (xpos, ypos)))
                self.counter += 1
        return self.graph


    def retracepath(goal):
        current = goal
        path = []

        while current:
             path.append(current)
             current = current.parent

        return path

