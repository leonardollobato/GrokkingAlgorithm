import sys

n = ["12","1012"]


def check(item):
    counter = 0
    s = item.strip()
    for i in range(0, len(s)):
        divisor = int(s[i])
        if divisor > 0 and int(item) % divisor == 0:
            counter += 1
    
    return counter

for i in range(0, len(n)):
    print(check(n[i]))


#print(check("1012"))
        



