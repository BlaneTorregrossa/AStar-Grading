from Bubble_sorting import Bubble


def sortscores(results, nodeaverage, costaverage):
    costscores = []
    nodescores = []
    finalscores = []
    na = nodeaverage
    ca = costaverage
    i = -1
    for r in results:
        i = i+1
        nodes = nodescore(results[i][1], na)
        nodescores.append(nodes)
        cost = costscore(results[i][0], ca)
        costscores.append(cost)
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
    nodelist1 = 
    nodelist2 = 
    nodelist3 = 
    result1 = ()
    result2 = ()
    result3 = ()
    results = []
    results.append(result1)
    results.append(result2)
    results.append(result3)
    sortscores(results, 5, 100)

def main():
    testsort()
main()