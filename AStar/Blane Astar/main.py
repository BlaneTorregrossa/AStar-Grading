# Change how modules are imported

#   Algorithm 1
import Blane_pathfinding_test
from Blane_pathfinding_test import blane_graph
from Blane_pathfinding_test import blane_astar

#   Algorithm 2 
import Christopher_pathfinding_test
from Christopher_pathfinding_test import christopher_graph
from Christopher_pathfinding_test import christopher_astar

#   Algorithm 3
import Christopher_AStar_test
from Christopher_AStar_test import christopheralt_graph
from Christopher_AStar_test import christopheralt_astar

#   Does not return anything but adds to lists
#   Needs smaller edits ***
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
    else:
        print("ERROR: Algorithm cannot be used! Does not meet specific requirments.")    

    expectedres = []
    for i in expected:
        expectedres.append(int(i.guid))

    actualres = []
    for i in result:
        actualres.append(int(i.guid))

    if actualres == expectedres:
        passcheck == True
    
    passlist.append(passcheck)
    actualpath.append(actualres)



#   To get the difference in position between each node of two paths 
#   and give a score based off of how close they are    ***
def getpathscore(algopath, expectedpath):
    missingnodes = 0
    extranodes = 0
    scorelist = []
    finalpathscore = 100
    scoresubtract = 0
    scorestandard = 100
    totalscores = []

    if len(algopath) > len(expectedpath):
        extranodes = (len(algopath) - len(expectedpath))
    elif len(algopath) < len(expectedpath)):
        missingnodes = (len(algopath) - len(expectedpath))
    
    testpathlength = len(algopath) - 1
    scoresubtract = finalpathscore / testpathlength

    #   Do this in reverse order    ***
    while testpathlength > 0:
        ydifference = abs(algopath[testpathlength][1] - expectedpath[testpathlength][1])
        xdifference = abs(algopath[testpathlength][0] - expectedpath[testpathlength][0])

        score = xdifference + ydifference
        scorelist.append(score)
        testpathlength -= 1
    

    # Scoring of each individual node and how close they are to expected position
    for i in range(0, len(scorelist)):
        if scorelist[i] < 0:
            totalscores.append(scorestandard)
        if scorelist[i] > 0:
            totalscores.append(scorestandard - scorelist[i])
            if totalscores[len(totalscores) - 1] < 0:
                totalscores[len(totalscores) - 1] = 0
    
#   Takes given results from the passfail and pathscore tests and creates a final grade
#   based off of the previous test results  ***
def finalgrade(pfresults, pathresults):
    pflength = len(pfresults)
    for i in pfresults:
        passscore = pflength / len(pathresults)

    # any additional math for pathresults

    passscore = passscore / 2
    pathresults = pathresults / 2
    
    return pathresults + passscore 

# standard insertion algorithm
def insertiontest(unarrangedlist):
    for i in range(1, len(unarrangedlist)):
        comparison = unarrangedlist[i]
        j = i-1

        while j >= 0 and comparison < unarrangedlist[j]:
            unarrangedlist[j+1] = unarrangedlist[j]
            j -= 1

        unarrangedlist[j+1] = comparison

# Set up for use with multiple algorithms ***
def main():

    test1 = [[43], [46], [95], [46, 45, 44, 43]]
    test2 = [[11], [67], [45, 55, 65, 75], [67, 56, 46, 35, 34, 33, 22]]
    test3 = [[82], [85], [76, 44, 11], [85, 74, 73, 82]]
    # test4 = 
    # test5 = 

    testlist = [test1, test2, test3]
    testsmax = len(testlist) - 1
    remainingtests = 0 
    currentresults = []
    givenpaths = []
    pathresults = []
    arrangement = []
    usedgraphs = [christopher_graph, blane_graph, christopheralt_graph]
    algolist = [christopher_astar, blane_astar, christopheralt_astar]

    # to go trough each test case in the list and run the test
    # Pass-Fail then path accuracy
    for i in range(0, len(algolist) - 1):
        while testsmax >= remainingtests:
            print(i)
            print("Pre Pass Fail")
            PassFail(currentresults, testlist[remainingtests],
                givenpaths, usedgraphs[i], algolist[i])
            print("Post Pass Fail")
            # getpathscore()
            remainingtests += 1
            # arrangement.append(finalgrade(currentresults, pathresults))


    #   Should name algorithm in list with score when written to file ***
    #   Algorithm names here are not accurate
    #   standard insertion
    insertiontest(arrangement)
    for i in range(len(arrangement)):
        with open('sortingresults.txt', 'a') as r:
            r.write('\n' + 'Algorithm ' + repr(i) +
            ' correctness: ' + repr(arrangement[i]))


if __name__ == '__main__':
    main()



