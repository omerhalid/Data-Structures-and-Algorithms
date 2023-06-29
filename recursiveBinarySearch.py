def recursive_binary_searc(list, target):
    first = 0
    last = len(list)-1

    if len(list) == 0:
        return False
    else:
        middle = (first + last) // 2

        if target == list[middle]:
            return True
        else:
            if target > list[middle]:
                return recursive_binary_searc(list[middle+1 : ], target)
            else:
                return recursive_binary_searc(list[:list[middle]], target)

isExist = recursive_binary_searc(numbers, 5)

print(isExist)
