# debug assignment 1

list1 = [1, 2, 3, 4, 5, 11, 20]
list2 = [6, 7, 8, 9]

combineBoth = [list1, list2]


for itemOfBothList in combineBoth:
    for item in itemOfBothList:
        if item < 12:
            itemOfBothList.remove(item)
            print(itemOfBothList)
