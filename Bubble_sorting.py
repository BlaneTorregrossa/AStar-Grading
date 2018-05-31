class Result(object):
    def __init__(self, value, lock)
    self.value = value
    self.lock = False

def Bubble(sortable):
    slist = sortable
    ordered = False
    for i in slist:
        ordered = isgreater(slist[i].value, slist[i + 1].value)
        if ordered == False

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
