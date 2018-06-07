import Bubble_sorting

def sortscores(results):
    costscores = []
    nodescores = []
    finalscores = []
    for r in results:
        nodes = nodescore(results[r].nodes)
        nodescores.append(nodes)
        cost = costscore(results[r].value)
        costscores.append(cost)
    nodescores = Bubble(nodescores, 10)
    costscores = Bubble(costscores, 10)

def costscore(cost):
    score = 100 - cost
    return score

def nodescore(path):
    pathnodes = countnodes(path)
    score = 7 - pathnodes
    return score 

def countnodes(path):
    nodecount = 0
    for each n in path:
        nodecount += 1
    return nodecount

def testsort():
    
    results = []