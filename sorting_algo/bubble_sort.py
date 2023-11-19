test_unordered_list = [6, 5, 3, 1, 8, 7, 2, 4]

# Bubble sort
# Time complexity: O(n^2)
# Space complexity: O(1)

# Bubble sort is a simple sorting algorithm that repeatedly steps through the list,
# compares adjacent elements and swaps them if they are in the wrong order.

# We start from the first element.
# We compare the first element with the second element.
# If the first element is greater than the second element, we swap them.
# We compare the second element with the third element.
# If the second element is greater than the third element, we swap them.

def bubble_sort(arr):
    n = len(arr)
    isSorted = True
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                isSorted = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if isSorted:
            break
    return arr

print(bubble_sort(test_unordered_list))