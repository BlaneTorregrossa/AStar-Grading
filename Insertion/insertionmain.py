
# standard insertion algo
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


# # Recursive insertion
# def insertiontest(unarrangedlist, num):
#     if num > 0:
#         insertiontest(unarrangedlist, num - 1)
#         comparison = unarrangedlist[num]
#         j = num - 1
#         while j >= 0 and unarrangedlist[j] > comparison:
#             unarrangedlist[j+1] = unarrangedlist[j]
#             j -= 1
#         unarrangedlist[j+1] = comparison



# this is where the given correctness values will be placed to be arranged
# numbers right here are place holders just to make sure sorting works correctlly
arrangement = [100, 22, 22, 3, 71, 85, 66, 200, 5]
insertiontest(arrangement)
# insertiontest(arrangement, len(arrangement) - 1)
for i in range(len(arrangement)):
    with open('Insertion\sortingresults.txt', 'a') as r:
        r.write('\n' + 'Algorithim ' + repr(i) +
         ' correctness: ' + repr(arrangement[i]))