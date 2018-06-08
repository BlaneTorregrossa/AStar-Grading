import Bubble_sorting

from Christopher_pathfinding import GRAPH

def sortscores(results, nodeaverage, costaverage):
    costscores = []
    nodescores = []
    finalscores = []
    na = nodeaverage
    ca = costaverage
    i = -1
    for r in results:
        i = i+1
        nscore = nodescore(results[i][0], na)
        nodescores.append(nscore)
        cscore = costscore(results[i][1], ca)
        costscores.append(cscore)
    nodescores = Bubble(nodescores, 10)
    costscores = Bubble(costscores, 10)

def costscore(cost, average):
    score = average - cost
    return score

def nodescore(path, average):
    pathnodes = countnodes(path)
    score = average - pathnodes
    return score 

def countnodes(path):
    nodecount = 0
    for n in path:
        nodecount += 1
    return nodecount

def testsort():
    nodelist1 = []
    nodelist2 = []
    nodelist3 = []
    result1 = (140, nodelist1)
    result2 = (50, nodelist2)
    result3 = (90, nodelist3)
    results = []
    results.append(result1)
    results.append(result2)
    results.append(result3)
    sortscores(results, 5, 100)

def main():
    testsort()
main()