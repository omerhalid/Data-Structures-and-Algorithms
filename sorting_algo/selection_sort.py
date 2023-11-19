test_unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4]

# Selection sort
# Time complexity: O(n^2)
# Space complexity: O(1)

# The algorithm divides the input list into two parts:
# the sublist of items already sorted, which is built up from left to right at the front (left) of the list,
# and the sublist of items remaining to be sorted that occupy the rest of the list.

# We find the smallest element in the unsorted sublist and swap it with the leftmost element,
# and then we increment the sublist boundary one element to the right.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort(test_unsorted_list))