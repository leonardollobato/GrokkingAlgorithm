# from selectionSort import sort
# from binarySearch import searchR
# from quickSort import quickSort
# NO 1040228318 438975792 1039690255 1295106684
# YES 933310691 1359233135 1149305470 512957173
# YES 702302686 684711731 1662063350 42927183
# YES 607436493 1499283941 2081952339 204670733
# YES 256722077 268325884 767545817 756696570

#  (a+b,b), (a,a+b)
#  (a-b,b), (a,a-b)

# 3 3 1 1

def walkThrough(arg1, arg2, final):
    
    if final >= arg1:
        sum = arg1 + arg2

        if sum < final:
            return walkThrough(sum, arg2, final)
        else:
            if sum == final:
                return True
            else:
                return False
    else:
        sum = arg1 - arg2

        if sum < final:
            return walkThrough(sum, arg2, final)
        else:
            if sum == final:
                return True
            else:
                return False
  
def canReach(array):
    if walkThrough(array[0],array[1],array[2]) and walkThrough(array[0],array[1],array[3]):
        return "TRUE"
    else:
        return "FALSE"


list  = [3,3,1,1]
list1  = [933310691, 1359233135, 1149305470, 512957173]
list2  = [702302686, 684711731, 1662063350, 42927183]
list3  = [607436493, 1499283941, 2081952339, 204670733]
list4  = [256722077, 268325884, 767545817, 756696570]

print(walkThrough(1,1,2))
print(walkThrough(1,1,3))

# print(canReach(list))
# print(canReach(list1))
# print(canReach(list2))
# print(canReach(list3))
# print(canReach(list4))

