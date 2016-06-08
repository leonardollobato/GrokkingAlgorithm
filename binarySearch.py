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


        