# Is it possible to swap out imported modules based on text file or application based action at runtime

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

#   Does not return anything but adds to lists
def PassFail(passlist, giventest, actualpath, givengraph, currentalgo):
    passcheck = False
    copygraph = list(givengraph)
    test = giventest
    start = copygraph[test[0][0]]
    goal = copygraph[test[1][0]]
    unwalkable = test[2]
    expected = []

    for i in test[3]:
        expected.append(copygraph[i])

    for i in unwalkable:
        copygraph[i].walkable = False

    if currentalgo:
        result = currentalgo(start, goal, copygraph)

    actualres = []
    for i in result:
        actualres.append(int(i.guid))

    if len(actualres) <= 0:
        passcheck = False
    elif actualres[len(actualres) - 1] == goal:
        passcheck = True
    
    passlist.append(passcheck)
    actualpath.append(actualres)

# simple node comparison
# Just checks if both lists match 
def getpathscore(algopath, expectedpath, comparelist):
    missingnodes = 0
    extranodes = 0
    scorelist = []
    returnpathscore = 100
    scoresubtract = 0
    scorestandard = 100
    totalscores = []

    # if len(algopath) > len(expectedpath):
    #     extranodes = (len(algopath) - len(expectedpath))
    # elif len(algopath) < len(expectedpath):
    #     missingnodes = (len(algopath) - len(expectedpath))
    
    testpathlength = len(algopath)
    if testpathlength > 0:
        scoresubtract = returnpathscore / testpathlength
    else:
         return 0

    counter = 0
    while counter != testpathlength:
        if algopath[counter] != expectedpath[counter]:
            returnpathscore -= scoresubtract
        else:
            pass
        counter += 1
    
    comparelist.append(float(returnpathscore))
    
    
#   Takes given results from the passfail and pathscore tests and creates a final grade
#   based off of the previous test results
def finalgrade(pfresults, pathresults):
    pflength = len(pfresults)
    removalnum = 0
    scorebase = 100
    finalpathscore = 0

    for i in pfresults:
        if pfresults[i - 1] == False:
            removalnum += 1
    if removalnum > 0:
        passscore = pflength / removalnum
    else:
        passscore = pflength / pflength

    pathscoresize = len(pathresults)
    while pathscoresize > 0:
        pathresults[pathscoresize - 1] = pathresults[pathscoresize - 1] / pathscoresize
        finalpathscore += pathresults[pathscoresize - 1]
        pathscoresize -= 1

    if pathscoresize != 0:
        finalpathscore = finalpathscore / pathscoresize

    passscore = float(passscore / 2)
    finalpathscore = float(finalpathscore / 2)

    return float(finalpathscore + passscore) 

# standard insertion algorithm
def insertiontest(unarrangedlist):
    for i in range(1, len(unarrangedlist)):
        comparison = unarrangedlist[i]
        j = i-1

        while j >= 0 and comparison < unarrangedlist[j]:
            unarrangedlist[j+1] = unarrangedlist[j]
            j -= 1

        unarrangedlist[j+1] = comparison

# Set up for use with multiple algorithms
def main():

    # reload(Christopher_pathfinding_test)
    # reload(Blane_pathfinding_test)

    test1 = [[43], [46], [95], [46, 45, 44, 43]]
    test2 = [[11], [67], [45, 55, 65, 75], [67, 56, 46, 35, 34, 33, 22]]
    test3 = [[82], [85], [76, 44, 11], [85, 74, 73, 82]]
    # test4 = 
    # test5 = 

    testlist = [test1, test2, test3]
    testsmax = len(testlist) - 1
    resultFile = "path and pass score.txt"
    remainingtests = 0 
    currentresults = []
    givenpaths = []
    comparisonresults = []
    arrangement = []
    usedgraphs = [christopher_graph, blane_graph]
    algolist = [christopher_astar, blane_astar]
    algorithmnames = ["Chris_AStar", "Blane_AStar"]

    # to go trough each test case in the list and run the test
    # Pass-Fail then path accuracy
    i = 0
    while i < len(algolist):
        while remainingtests <= testsmax:
            PassFail(currentresults, testlist[remainingtests],
                givenpaths, usedgraphs[i], algolist[i])
            getpathscore(givenpaths[i], testlist[remainingtests - 1], comparisonresults)
            remainingtests += 1
        i += 1
        remainingtests = 0
        arrangement.append(finalgrade(currentresults, comparisonresults))


    #   standard insertion
    insertiontest(arrangement)
    towrite = len(arrangement)
    counter = 0
    open(resultFile, 'w').close()
    while counter <= towrite:
        with open(resultFile, 'a') as r:
            r.write('\n' + repr(algorithmnames[counter - 1]) +
            ' correctness: ' + repr(arrangement[counter - 1]))
        counter += 1
    
    showinfo('Testing Done', "Result written out on document named: " + resultFile)

main()



