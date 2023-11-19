test_list_unsorted = [6, 5, 3, 1, 8, 7, 2, 4]

#Insertion sort
#Time complexity: O(n^2)
#Space complexity: O(1)

#Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
#We insert each element onto its correct position.
#We start from the second element.
#We compare the second element with the first element.
#If the second element is smaller than the first element, we swap them.

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        value = arr[i]
        hole = i
        while hole > 0 and arr[hole-1] > value:
            arr[hole] = arr[hole - 1]
            hole -= 1
        arr[hole] = value
    return arr
    
print(insertion_sort(test_list_unsorted))