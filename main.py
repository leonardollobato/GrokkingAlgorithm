from selectionSort import sort
from binarySearch import searchR

numbers = [6,3,18,9,5,1,2,7,4]
sortedNumber = sort(numbers)
print(sortedNumber)
print(searchR(sortedNumber,18, (len(sortedNumber) - 1)))
#print(sortedNumber)
#print(search(sortedNumber,6))

def sum(array):
    if len(array) == 0:
        return 0
    else:
        item = array.pop(0)
        return item + sum(array)

def size(list):
    if list == []:
        return 0
    else:
        index = list.pop(0)
        return 1 + size(list)

def max(list):
    if list == []:
        return None
    elif len(list) == 1:
        return list[0]
    else:
        if list[0] >= list[1]:
            list.pop(1) 
        else:
            list.pop(0)
    
    return max(list)


        
#print(max(sortedNumber))


    
