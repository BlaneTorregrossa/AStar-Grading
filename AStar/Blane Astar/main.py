import pathfinding
from pathfinding import GRAPH
from pathfinding import astar


def PassFail(passlist, giventest, actualpath):
    passcheck = False
    copygraph = list(GRAPH)
    test = giventest
    start = copygraph[test[0][0]]
    goal = copygraph[test[1][0]]
    unwalkable = test[2]
    expected = []
    for i in test[3]:
        expected.append(copygraph[i])

    for i in unwalkable:
        copygraph[i].walkable = False

    # this needs to swap with the astar function being tested   ***
    result = astar(start, goal, copygraph)

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

   
# Can not figure out a good way to calculate path acurracy that makes sense ***
# I want this to calculate score not nodes that are over/under expected range
# what is here is extremely simplified and doesn't consider score only size and checks if the nodes are the same
# this is not good for getting a final score
# and it also doesn't work because this is in place of what I want for this function

# def pathcorrectness(expectedpath, algopath):
    
    # What I Want: 
    # A way to get rate accuracy of path given by algorithm based on score and giving a score on difference based on expected path

    # What I Got:
    # Nothing that works or makes since and a node comparison that doesn't even work because of me trying to have something after failing to achieve the above
    # MOVE ONTO USING A MINI ASTAR ALGO TO CHECK SELECTED NODES
    
    # counter = 0
    # if len(expectedpath) >= len(algopath):
    #     for i in expectedpath:
    #         if algopath[i] != expectedpath[i]:
    #             score = (len(expectedpath) - 1) - counter
    #         else:
    #             counter += 1
    
    # elif len(algopath) > len(expectedpath):
    #     for i in algopath:
    #         if algopath[i] != algopath[i]:
    #             score = (len(algopath) - 1) - counter
    #         else:
    #             counter += 1

    # return score
            

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

    #Traverse trough 1 to the length of arrangement
    for i in range(1, len(unarrangedlist)):
        comparison = unarrangedlist[i]
        # move elements of arrangement to one position
        # ahead of their current position, if greater than comparison
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
    
    testlist = [test1, test2, test3]
    remainingtests = len(testlist)
    currentresults = []
    givenpaths = []
    pathresults = []
    arrangement = []

    while remainingtests > 0:
        PassFail(currentresults, testlist[remainingtests - 1], givenpaths)
        currenttest = testlist[remainingtests - 1]
        # pathresults.append(pathcorrectness(currenttest[3], currenttest[3])) #   *** Call for function that doesn't work
        remainingtests -= 1

    arrangement.append(finalgrade(currentresults, pathresults)

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



