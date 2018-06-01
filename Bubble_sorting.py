class Result(object):
    def __init__(self, value, lock)
    self.value = value
    self.lock = False

def Bubble(sortable):
    slist = sortable
    ordered = False
    
        

def swapplaces(pos1, pos2, num1, num2, sortable):
    slist = sortable
    slist[pos1] = num2
    slist[pos2] = num1
    return slist

def isgreater(num1, num2):
    if num1 > num2:
        return True
    else:
        return False

def findgreatest(slist):
    high = 0
    for i in slist:
        if slist[i] > high:
            high = slist[i]
    return high

def sort(slist):
    for i in slist:
        ordered = isgreater(slist[i].value, slist[i + 1].value)
        if ordered == True:
            swapplaces(i, i + 1, slist[i].value, slist[i + 1].value)