#come back to this one

#Non-Divisible Subset
#https://www.hackerrank.com/challenges/non-divisible-subset/problem

#Problem statement:
#Given a set of distinct integers, print the size of a maximal subset of S where the sum of any 2 numbers in S' is not evenly divisible by k.

# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Step 1: Create a list to hold the counts of remainders of elements of `s` when divided by `k`.
    remainder_counts = [0] * k
    
    # Step 2: For each number in `s`, compute its remainder when divided by `k` and increment the count for that remainder.
    for num in s:
        remainder_counts[num % k] += 1

    # Step 3: Initialize a variable `count` with a value of `0`.
    count = 0
    
    # Step 4: For each possible remainder `i` (from `1` to `k/2`), pick the larger count between counts of remainders `i` and `k-i`.
    for i in range(1, k // 2 + 1):
        if i != k - i:
            count += max(remainder_counts[i], remainder_counts[k - i])

    # Step 5: If there's at least one number in `s` that's divisible by `k` (remainder 0), add `1` to the `count`.
    if remainder_counts[0] > 0:
        count += 1

    # Step 6: Return the `count`.
    return count