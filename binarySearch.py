def search(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) / 2
        guess = list[mid] 

        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return mid

    return None


def searchR(list, item, counter):
    if list == []:
        return None
    elif len(list) == 1:
        if list[0] ==  item:
            return 0
        else:
            return None
    else:
        if list[counter] == item:
            return counter
        else:
            counter = counter - 1
            return searchR(list, item, counter)




        