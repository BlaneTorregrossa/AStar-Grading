import pathfinding

# # to gather correctness based on given bath
# def gatherpathcorrectness(expectedscore):
#     testpath = pathfinding.astar(GRAPH[0], GRAPH[99], GRAPH)
#     goalnode = len(testpath)
#     score = testpath[goalnode].f
#     if score > expectedscore:
#         # compare paths

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


# # Recursive insertion algorithm
# def insertiontest(unarrangedlist, num):
#     if num > 0:
#         insertiontest(unarrangedlist, num - 1)
#         comparison = unarrangedlist[num]
#         j = num - 1
#         while j >= 0 and unarrangedlist[j] > comparison:
#             unarrangedlist[j+1] = unarrangedlist[j]
#             j -= 1
#         unarrangedlist[j+1] = comparison


#   this is where the given correctness values are to be placed to be arranged
#   numbers right here are place holders just to make sure sorting works correctlly
arrangement = [100, 22, 22, 3, 71, 85, 66, 200, 5]
#   standard insertion
insertiontest(arrangement)
#   Recursive Insertion
# insertiontest(arrangement, len(arrangement) - 1)
for i in range(len(arrangement)):
    with open('AStar\Blane AStar\sortingresults.txt', 'a') as r:
        r.write('\n' + 'Algorithm ' + repr(i) +
         ' correctness: ' + repr(arrangement[i]))