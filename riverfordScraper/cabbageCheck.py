def containsCababage(boxContents):
    """Returns true or false as to whether there are any types of
    cabbage in the given box"""
    for item in boxContents:
        if 'cabage' in item:
            return True

def findAlternativeBoxes(boxesInfo, allowedBoxes):
    """Searches for boxes from the specified list containing no cabbage"""
    cabbageFreeBoxes=[]
    for boxName, items in boxesInfo.iteritems():
        if boxName in allowedBoxes and not containsCababage(items):
            cabbageFreeBoxes.append(boxName)
    return cabbageFreeBoxes