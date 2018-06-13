# this is the restructuring of this whole file
# Right now cutting out everything that is useless

# Should have to import testing and scoring. Should not be in main.

import sys

from tkMessageBox import *
from os.path import join

#   Algorithm 1 The busted one
import Blane_pathfinding_test
from Blane_pathfinding_test import blane_graph
from Blane_pathfinding_test import blane_astar

#   Algorithm 2 The working one
import Christopher_pathfinding_test
from Christopher_pathfinding_test import christopher_graph
from Christopher_pathfinding_test import christopher_astar


# standard insertion algorithm
def insertiontest(unarrangedlist):
    for i in range(1, len(unarrangedlist)):
        comparison = unarrangedlist[i]
        j = i-1
        while j >= 0 and comparison < unarrangedlist[j]:
            unarrangedlist[j+1] = unarrangedlist[j]
            j -= 1

        unarrangedlist[j+1] = comparison

# Set up for how the window is created here. Actions are defined in methods
def main():

    test1 = [[43], [46], [95], [46, 45, 44, 43]]
    test2 = [[11], [67], [45, 55, 65, 75], [67, 56, 46, 35, 34, 33, 22]]
    test3 = [[82], [85], [76, 44, 11], [85, 74, 73, 82]]
    # test4 = 
    # test5 = 
    # ...

    testlist = [test1, test2, test3]
    testsmax = len(testlist) - 1
    resultFile = "sorted scores.txt"
    remainingtests = 0 
    currentresults = []
    givenpaths = []
    comparisonresults = []
    arrangement = [0.80, 0.25]  # placeholders
    usedgraphs = [christopher_graph, blane_graph]
    algolist = [christopher_astar, blane_astar]
    algorithmnames = ["Chris_AStar", "Blane_AStar"]

    #   standard insertion
    insertiontest(arrangement)
    towrite = len(arrangement)
    counter = 0
    open(resultFile, 'w').close()
    while counter < towrite:
        with open(resultFile, 'a') as r:
            r.write('\n' + repr(arrangement[counter - 1]))
        counter += 1

main()



