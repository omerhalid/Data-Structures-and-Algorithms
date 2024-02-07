# Quick sort algorithm

# Divide and conquer algorithm
    # Breaks down a problem into smaller chunks
    # Solutions to the sub-problems are then combined to give a solution to the original problem
    
# Run time depends on the pivot selection
    # Best case: O(n log n)
    # Worst case: O(n^2)
    
# Steps:
    # choose a pivot (usually the last element)
    # stores elements smaller than the pivot to the left
    # stores elements greater than the pivot to the right
    # call quicksort on the left and right sub-arrays recursively
    # then you will end up with a sorted array
    
    # 2 pointers i and j
    # i starts at the first element (low)
    # j starts at the second to last element (high - 1)
    # pivot is the last element (high)
    # for each j from low to high - 1
    #   if arr[j] < pivot, increment i and swap arr[i] and arr[j]
    # after the loop, swap arr[i+1] and arr[high] (pivot)
    # return i + 1 as the pivot index
    
# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quicksort(left) + middle + quicksort(right)

# print(quicksort([3,6,8,10,1,2,1]))

def quicksort(arr, left, right):
    if left<right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot - 1)
        quicksort(arr, pivot + 1, right)
        
def partition(arr, left, right):
    i = left
    j = right - 1
    
    pivot = arr[right]
    
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
            
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            
    arr[i], arr[right] = arr[right], arr[i]
    
    return i


data = [9,4,8, 1, 2, 10]
quicksort(data, 0, len(data)-1)
print(data)

def binary_search(arr, data):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (right + left) // 2
        if data == arr[mid]:
            return True
        
        elif data>arr[mid]:
            left = mid + 1
        
        elif data<arr[mid]:
            right = mid - 1

    return False

print(binary_search(data, 10)) # True
print(binary_search(data, 3)) # False