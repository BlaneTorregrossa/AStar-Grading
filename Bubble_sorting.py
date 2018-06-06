class Result(object):
    def __init__(self, value, lock)
    self.value = value
    self.lock = False

def Bubble(sortable):
    '''Need to sort through every value in the list. Locking the highest number into place when 
    it reaches the end of the list and repeating this process until finally the whole list is locked'''
    slist = sortable
    sortloop(slist)

def swapplaces(pos1, pos2, num1, num2, sortable):
    '''swaps the positon of the two values in the list'''
    slist = sortable
    slist[pos1] = num2
    slist[pos2] = num1
    return slist

def isgreater(num1, num2):
    '''checks to see if the one number is greater than the other'''
    if num1 > num2:
        return True
    else:
        return False

def findgreatest(slist):
    '''Find the highest unlocked value in the list'''
    high = 0
    for i in slist:
        if slist[i].value > high
            high = slist[i]
    return high

def sortloop(slist):
    '''loops through the list once and sorts it'''
    for i in slist:
        notordered = isgreater(slist[i].value, slist[i + 1].value)
        if notordered == True:
            swapplaces(i, i + 1, slist[i].value, slist[i + 1].value)

'def lockvalue(res):
    '''sets the value's lock to True'''
    'val.lock = True