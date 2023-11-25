#come back here

def binary_search(list, target):
    first = 0
    last = len(list)-1

    while (first <= last):
        middle = (last + first) // 2
        if target == list[middle]:
            return middle
        elif target > list[middle]:
            first = middle + 1
        else:
            last = middle - 1
    return None

list = [1,2,3,4,5,6,7,8,9]
target = 6
print(binary_search(list, target))