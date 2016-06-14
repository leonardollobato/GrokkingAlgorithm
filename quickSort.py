def quickSort(array):
    if len(array) < 2:
        return array
    else:
        mid = (len(array)/2)
        pivot = array[mid]
        lower = []
        higher = []

        for i in range(0, len(array)):
            if i != mid:
                if array[i] > pivot:
                    higher.append(array[i])
                else:
                    lower.append(array[i])
        
        return quickSort(lower) + [pivot] + quickSort(higher)





