#Forming a 3x3 magic square
#https://www.hackerrank.com/challenges/magic-square-forming/problem

#Problem statement:
#We define a magic square to be an n x n matrix of distinct positive integers from 1 to n^2 where the sum of any row, column, or diagonal of length n is always equal to the same number: the magic constant.

#High level solution:
#1. Create a list of all possible magic squares. But how? We can create a list of all possible 3x3 magic squares and store them in a list. Why 3x3? Because the input is a 3x3 matrix.
#2. Iterate through the list and find the difference between the given square and each magic square
#3. Return the minimum difference

#Time complexity: O(n^2)
#Space complexity: O(n^2)

def formingMagicSquare(s):
    # All 8 possible 3x3 magic squares
    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]

    min_cost = float('inf')  # Initialize to a large value

    for magic in magic_squares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(s[i][j] - magic[i][j])
        min_cost = min(min_cost, cost)

    return min_cost
