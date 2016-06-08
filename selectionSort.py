
def findSmallest(list):

    smallest = list[0]
    smallest_index = 0

    for i in range(1, len(list)):
        if smallest > list[i]:
            smallest = list[i]
            smallest_index = i

    return smallest_index


def sort(list):
    sortedList = []
    for i in range(0, len(list)):
        index = findSmallest(list)
        sortedList.append(list.pop(index))
    
    return sortedList


