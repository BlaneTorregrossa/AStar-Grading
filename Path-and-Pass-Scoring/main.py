# lots of importing to be done here

import sys
from tkMessageBox import *

#   Algorithm 1
from Blane_pathfinding_test import blane_graph
from Blane_pathfinding_test import blane_astar

#   Algorithm 2
from Christopher_pathfinding_test import christopher_graph
from Christopher_pathfinding_test import christopher_astar

#   Does not return anything but adds to lists
#   Rework  *** 
def PassFail(passlist, giventest, actualpath, givengraph, currentalgo):
    passcheck = False
    copygraph = list(givengraph)
    test = giventest
    start = copygraph[test[0][0]]
    goal = copygraph[test[1][0]]
    unwalkable = test[2]

    result = currentalgo(start, goal, copygraph)

    actualres = []
    for node in result:
        actualres.append(int(node.guid))
        if actualres[0] == goal:
            passcheck == True
            passlist.append(passcheck)
            actualpath.append(actualres)
            return

    passlist.append(passcheck)
    actualpath.append(actualres)

# simple node comparison
# Just checks if both lists match 
# Rework    ***
def getpathscore(algopath, expectedpath, comparelist):
    missingnodes = 0
    extranodes = 0
    scorelist = []
    returnpathscore = 100
    scoresubtract = 0
    scorestandard = 100
    totalscores = []

    maxcount = 0
    if len(algopath) > len(expectedpath) or len(algopath) == len(expectedpath):
        maxcount = len(expectedpath) - 1
        counter = 0
        while counter != maxcount:
            if algopath[counter] != expectedpath[counter]:
                returnpathscore -= scoresubtract
            counter += 1
    if len(expectedpath) > len(algopath):
        maxcount = len(algopath)
        counter = 0
        while counter != maxcount:
            if algopath[counter] != expectedpath[counter]:
                returnpathscore -= scoresubtract
            counter += 1

    comparelist.append(float(returnpathscore))
    
    
#   Takes given results from the passfail and pathscore tests and creates a final grade
#   based off of the previous test results
#   Rework  ***
def finalgrade(pfresults, pathresults, algoname, pffile, pafile):
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
    finalpathscore = (float(finalpathscore / 4) / 100) 

    return float(finalpathscore + passscore) 

#   standard insertion algorithm
#   *** Sperate
def insertion(unarrangedlist):
    for i in range(1, len(unarrangedlist)):
        comparison = unarrangedlist[i]
        j = i-1

        while j >= 0 and comparison < unarrangedlist[j]:
            unarrangedlist[j+1] = unarrangedlist[j]
            j -= 1

        unarrangedlist[j+1] = comparison

#   ***
def writeresults(givenlist, givenfile, giventitle):
    towrite = len(givenlist) - 1
    counter = 0
    while counter <= towrite:
        with open(givenfile, 'a') as r:
            r.write('\n' + repr(giventitle) + repr(givenfile) + repr(givenlist))


# Rework    ***
# Set up for use with multiple algorithms
# almost everything should go trough
def main():

    test1 = [[43], [46], [95], [46, 45, 44, 43]]
    test2 = [[11], [67], [45, 55, 65, 75], [67, 56, 46, 35, 34, 33, 22]]
    test3 = [[82], [85], [76, 44, 11], [85, 74, 73, 82]]
    # test4 = 
    # test5 = 
    # ...

    testlist = [test1, test2, test3]
    testsmax = len(testlist) - 1
    resultFile = "Final Grade.txt"
    passfailresultFile = "Pass Fail Score.txt"
    pathaccuracyresultFile = "Path Accuracy Score.txt"
    dumpingFile = "dump.txt"
    #   ***

    remainingtests = 0 
    currentresults = []
    givenpaths = []
    comparisonresults = []
    arrangement = []
    usedgraphs = [blane_graph, christopher_graph]
    algolist = [blane_astar ,christopher_astar]
    names = ['Blane_pathfinding', 'Chris_pathfinding']

    open(resultFile, 'w').close
    open(passfailresultFile, 'w').close
    open(pathaccuracyresultFile, 'w').close
    open(dumpingFile, 'w').close

    # to go trough each test case in the list and run the test
    # Pass-Fail then path accuracy
    i = 0
    while i < len(algolist):
        while remainingtests <= testsmax:
            PassFail(currentresults, testlist[remainingtests],
                givenpaths, usedgraphs[i], algolist[i])
            getpathscore(givenpaths[i], testlist[remainingtests - 1], comparisonresults)
            remainingtests += 1
        arrangement.append(finalgrade(currentresults, comparisonresults, names[i], passfailresultFile, pathaccuracyresultFile))
        i += 1
        remainingtests = 0

    #sorting and then writting to file
    insertion(arrangement)
    towrite = len(arrangement) - 1
    counter = 0
    while counter <= towrite:
        with open(resultFile, 'a') as r:
            r.write('\n' + repr(names[counter - 1]) +
            ' correctness: ' + repr(arrangement[counter - 1]))
        counter += 1
    
    # Pop up window at the end of the method once results have been gathered and written to a given file
    # This is to inform the user that a document has been created/updated to include the results of tested algorithm 
    showinfo('Testing Done', "Result written out on document named: " + resultFile)
    
    

main()



