#   Algorithm 1
import pathfinding
from pathfinding import GRAPH 
from pathfinding import astar

#   Algorithm 2 Missing ***
# import astaralgo

def PassFail(passlist, giventest, actualpath, givengraph, currentalgo):
    passcheck = False
    copygraph = list(graph)
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
    print str.format('start::{0} goal::{1} unwalkables::{2}', start, goal, unwalkable)

    actualres = []
    for i in result:
        actualres.append(int(i.guid))
    print str.format('expected result {0} \nactual   result {1}', expectedres, actualres)

    if actualres == expectedres:
        passcheck == True
    
    passlist.append(passcheck)
    actualpath.append(actualres)


#   ***
def getpathscore(algopath, expectedpath):
    pass
    
#   ***
def finalgrade(pfresults, pathresults):
    pflength = len(pfresults)
    for i in pfresults:
        if pfresults[i - 1] == False:
            pflength -= 1
        else:
            pass
    
    passscore = pflength / len(pfresults)

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
    remainingtests = len(testlist)
    currentresults = []
    givenpaths = []
    pathresults = []
    arrangement = []
    usedgraphs = [GRAPH]
    algolist = [astar]

    # to go trough each test case in the list and run the test
    # Pass-Fail then path accuracy
    while remainingtests > 0:
        PassFail(currentresults, testlist[remainingtests - 1],
         givenpaths, usedgraphs[0], algolist[0])
        currenttest = testlist[remainingtests - 1]
        # getpathscore(givenpaths, currenttest[2])
        remainingtests -= 1

    arrangement.append(finalgrade(currentresults, pathresults))

    #   Should name algorithm in list with score when written to file
    #   standard insertion
    insertiontest(arrangement)
    for i in range(len(arrangement)):
        with open('sortingresults.txt', 'a') as r:
            r.write('\n' + 'Algorithm ' + repr(i) +
            ' correctness: ' + repr(arrangement[i]))


if __name__ == '__main__':
    main()



