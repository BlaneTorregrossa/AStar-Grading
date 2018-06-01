import node
from node import Node           #imports Node class from node.py

#columns and rows for a graph/grid
#preferbly 5x5 
class Graph(object):
    def __init__(self, row, col):
        self.columns = col
        self.rows = row
        self.nodes = []
        self.gengraph()
        
    def gengraph(self):
        counter = 0
        for xpos in range(0, self.rows):
            for ypos in range(0, self.columns):
                newnode = Node([xpos, ypos], counter)
                counter = counter + 1
                self.nodes.append(newnode)
    
    