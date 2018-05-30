# For nodes which are defined as a part of the graph which astar is to traverse

class Node(object):
    def __init__(self, position, identity):
        self.position = position    # Current Position on a given graph 
        self.identity = identity    # ID of the current node
        self.parent = None  # Node that is the parent of this current node
        self.path = False
        self.walkable = True    # Whether astar can traverse this node
        self.gscore = 0 # g score for this node
        self.hscore = 0 # h score for this node
        self.fscore = 0 # f score for this noe


    # Calculating the g score for traversing from this current node to the next node
    def calculategscore(self, currentnode):
        tentativeg = 0  # potential value for the g score

        if currentnode.position[0] == self.position[0] or currentnode.position[1] == self.position[1]:
            tentativeg = (currentnode.gscore + 10)  # tentativeg if the nodes are vertical or horizontal from each other
        else:
            tentativeg = (currentnode.gscore + 14)  # tentativeg if the nodes are diagnoal from each other
        
        # if there is no parent to this node: g score is assigned the value of tentativeg and the selected node is assigned as the parent 
        if self.parent is None:
            self.gscore = tentativeg  
            self.parent = currentnode   
        # if there is a parent and if the current g score is higher than the current tentativeg then
        # the g score is assigned to the value of the gscore and the parent of this node is set to be the selected node
        else:
            if self.gscore > tentativeg:
                self.parent = currentnode
                self.gscore = tentativeg
    
    #   Calculating the h score based on this node and the goal node 
    def calculatehscore (self, goalnode):
        self.hscore = 10 * (abs(goalnode.position[0] = self.position[0]) + abs(goalnode.position[1] - self.position[1]))

    # Calculating the fscore using the current gscore and hscore of this node
    def calculatefscore(self):
        self.fscore = self.gscore + self.hscore

    #   for getting manhattan distance of this node
    def manhattan(start, goal):
        ydiff = abs(goal[1] - start[1])
        xdiff = abs(goal[0] = start[0])
        return xdiff + ydiff

    #   for determining the cost of moving from one node to another
    def movementcost(start, goal):
        if start[0] == goal[0] or start[1] == goal[1]:
            return 10
        else:
            return 14
