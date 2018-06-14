from Bubble_sorting import Bubble

class Pathscores(object):
    def __init__(self, nodelist, totalcost):
        self.nodelist = nodelist
        self.totalcost = totalcost
        self.nodenum = countnodes(nodelist)

def sortscores(results, nodeaverage, costaverage):
    #Sorts the list of results by the combined total of their node score and their cost score
    

def costscore(cost, average):
    #determines a path's cost score

def nodescore(path, average):
    #determines a path's node score


def countnodes(path):
    #counts the nodes in a path
    nodecount = 0
    for n in path:
        nodecount += 1
    return nodecount

def testsort():

def main():
    testsort()
main()