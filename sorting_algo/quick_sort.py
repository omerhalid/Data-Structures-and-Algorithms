# Quick sort algorithm

# Divide and conquer algorithm
    # Breaks down a problem into smaller chunks
    # Solutions to the sub-problems are then combined to give a solution to the original problem
    
# Run time depends on the pivot selection
    # Best case: O(n log n)
    # Worst case: O(n^2)

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quicksort(left) + middle + quicksort(right)

# print(quicksort([3,6,8,10,1,2,1]))

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

data = [3,6,8,10,1,2,1]
quicksort(data, 0, len(data)-1)
print(data)