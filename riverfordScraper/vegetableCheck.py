def containsVegetable(vegetable, boxContents):
    """Returns true or false as to whether there are any types of
    cabbage in the given box"""
    for item in boxContents:
        if vegetable in item.lower():
            return True
    return False


def findAlternativeBoxes(vegetable, boxesInfo, allowedBoxes):
    """Searches for boxes from the specified list containing no cabbage"""
    cabbageFreeBoxes = []
    for boxName, items in boxesInfo.iteritems():
        if boxName in allowedBoxes and not containsVegetable(vegetable, items):
            cabbageFreeBoxes.append(boxName)
    return cabbageFreeBoxes
