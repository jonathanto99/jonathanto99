import sys

def listSum(list1):
    list1.append(6)
    for i in list1:
        total = 0
        total += i
        return total

list2 = [1, 2, 4, 5]
print(len(listSum(list2)))
