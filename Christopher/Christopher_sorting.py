from Christopher_pathfinding import astar
from Christopher_pathfinding import testfunc
from Christopher_pathfinding import GRAPH
from Christopher_AStar import pathcost
from Bubble_sorting import Result
from Bubble_sorting import Bubble

def main():
    failcount = 0
    passcount = 0
    valuelist = []
    for _ in range(10):
        res = testfunc(astar(GRAPH[4], GRAPH[25], GRAPH))
        if res:
            passcount += 1
            newvalue = pathcost(astar(GRAPH[4], GRAPH[25], GRAPH))
            valuelist.append(newvalue)
        else:
            failcount += 1
    print str.format('fails {0}, passes {1}', failcount, passcount)
    Bubble(valuelist, 10)
     
if __name__ == '__main__':
    main()
