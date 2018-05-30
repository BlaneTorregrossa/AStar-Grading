class Astar(object):
    def __init__(self):

    
    def run(start, goal, graph):
        current = start
        openlist = [current]
        closedlist = []
        path = []

        while openlist:
            openlist.remove(current)
            closedlist.append(start)

            