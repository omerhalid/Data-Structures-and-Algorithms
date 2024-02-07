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

# sorted_list = [1, 2, 3, 4, 5]

# def binary_search(sorted_list, index):
#     #find the middle
#     #check if it is smaller or greater then index
#     #if index is smaller than the middle go and search in the first half (the new list is [0:middle-1]
#     #if index is greater than the middle go and search in the second half (the new list is [middle+1:]
    
#     middle = len(sorted_list) // 2 
    
#     if len(sorted_list) == 0:
#         return False
    
#     if index == sorted_list[middle]:
#         return True
#     elif index > sorted_list[middle]:
#         return binary_search(sorted_list[middle+1:], index)
#     else:
#         middle = middle - 1
#         return binary_search(sorted_list[:middle+1], index)
    