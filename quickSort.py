numbers = [6,3,18,9,5,1,2,7,4]

def quickSort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = []
        greater = []

        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]

        return quickSort(less) + [pivot] + quickSort(greater)






print quickSort(numbers)

        