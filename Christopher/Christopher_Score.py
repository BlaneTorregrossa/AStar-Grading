from Bubble_odescore())
class Pathresults(object):
    def __init__(self, nodelist, totalcost):
        self.nodelist = nodelist
        self.totalcost = totalcost
        self.nodenum = countnodes(nodelist)
        self.ns = 0 #node score
        self.cs = 0 #cost score

def sortscores(resultslist, nodeaverage, costaverage):
    #Sorts the list of results by the combined total of their node score and their cost score
    for r in resultslist:
        resultslist[r].ns = nodescore(resultslist[r].nodenum, nodeaverage)
        resultslist[r].cs = costscore(resultslist[r].totalcost, costaverage)

def costscore(cost, average):
    #determines a path's cost score
    score = average - cost
    return score

def nodescore(nodes, average):
    #determines a path's node score
    score = average - nodes
    return score

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