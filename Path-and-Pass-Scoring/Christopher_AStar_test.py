import math

class Node(object):
    '''node'''
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
        '''overload string for print'''
        return "guid: " + self.guid + "\nPosition " + str(self[0]) + ", " + str(self[0])

def retrace(start, goal):

    path = []
    current = goal
    while current.parent is not None:
        path.append(current)
        current = current.parent
    if current.parent is None:
        path.append(current)
    return path

def printpath(path):
    for i in path:
        print 'Node: ', i.guid
    f = pathcost(path)

def pathcost(path):
    cost = 0
    for i in path:
        cost = cost + i.f
    return cost

def get_neighbors(current, nodes):
    '''get the neighbors    nodes the list of nodes to check    current the node to check nodes with'''
    # directions
    '''put those in a list'''
    '''loop over that list'''
    '''make a tuple that represents the node as a direction'''
    # example bob = Node("bob", 1, 2)
    #(1,2) != bob
    #(1,2) == (bob[0], bob[0])
    #if we get an equality then add the actual node to the neighbors list
    right = (current[0] + 1, current[1])
    top_right = (current[0] + 1, current[0] + 1)
    top = (current[0], current[0] + 1)
    top_left = (current[0] - 1, current[0] + 1)
    left = (current[0] - 1, current[0])
    bottom_left = (current[0] - 1, current[0] - 1)
    bottom = (current[0], current[0] - 1)
    bottom_right = (current[0] + 1, current[0] - 1)
    directions = [right, top_right, top, top_left, left, bottom_left, bottom, bottom_right]
    neighbors = []
    for i in nodes:
        node = (i[0], i[0])
        if node in directions:
            neighbors.append(i)
    return neighbors

def find_g(node, neighbor):
    gcost = 0
    if neighbor[0] == node[0] or neighbor[0] == node[0]:
        gcost = 10
    else:
        gcost = 14
    return gcost

def find_h(node, goal):
    return 10 * (abs(node[0] - goal[0]) + abs(node[0] - goal[0]))

def christopheralt_astar(graph, start, goal):
    path = []
    current = start
    openlist = []
    closedlist = []
    openlist.append(current)
    while goal not in closedlist:
        closedlist.append(current)
        openlist.remove(current)
        for neighbor in get_neighbors(current, graph):
            neighbor.g = current.g + find_g(current, neighbor)
            tentative_g = neighbor.g
            if neighbor in closedlist:
                    continue
            if neighbor not in openlist:
                neighbor.g = find_g(current, neighbor) + current.g
                neighbor.parent = current
                openlist.append(neighbor)
            else:
                if tentative_g >= neighbor.g:
                    continue
                else:
                    neighbor.g = tentative_g + current.g
                    neighbor.parent = current
            neighbor.h = find_h(neighbor, goal)
            neighbor.f = neighbor.g + neighbor.h
        # openlist.sort(key=lambda node: node.f)
        current = openlist[0]
        if current == goal:
            path = retrace(start, goal)
    return path


christopheralt_graph = []
COUNT = 0
for ypos in range(10):
    for xpos in range(10):
        christopheralt_graph.append(Node(COUNT, (xpos, ypos)))
        COUNT += 1


def main():
    test = christopheralt_astar(christopheralt_graph, christopheralt_graph[4], christopheralt_graph[25]) 
    printpath(test)   

if __name__ == '__main__':
    main()