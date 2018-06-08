import Bubble_sorting

def sortscores(results):
    costscores = []
    nodescores = []
    finalscores = []
    for r in results:
        nodes = nodescore(results[r].nodes, 5)
        nodescores.append(nodes)
        cost = costscore(results[r].value, 100)
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
    for each n in path:
        nodecount += 1
    return nodecount

def testsort():
    result1(160, 10)
    result2(90, 5)
    result3(200, 7)
    results = []
    results.append(result1)
    results.append(result2)
    results.append(result3)
    sortscores(results)

def main():
    testsort()
main()