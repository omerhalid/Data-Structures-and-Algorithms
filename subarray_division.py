#Subarray division problem from HackerRank
# Link: https://www.hackerrank.com/challenges/the-birthday-bar/problem

# The birthday bar hackerrank solution python


# 2nd solution with sliding window
# sliding window technique is useful when you need to find a contiguous subarray or a contiguous data set of some sort within a larger data structure.

def birthday(s, d, m):
    i = 0
    j = m
    
    counter = 0
    
    while j <= len(s):
        if sum(s[i:j]) == d:
            counter += 1
        i += 1
        j += 1

    return counter


# High level solution for the below code:
# 1. Iterate through each possible starting point for a segment in s
# 2. Get the segment of length m starting from i
# 3. If the segment is valid, increment counter
# 4. Return counter

def birthday(s, d, m):
    counter = 0
    # Iterate through each possible starting point for a segment in s
    for i in range(len(s) - m + 1):
        # Get the segment of length m starting from i
        segment = s[i:i+m]
        
        # If the segment is valid
        if sum(segment) == d:
            counter += 1
            
    return counter

