#Fair rations problem from HackerRank
# Link: https://www.hackerrank.com/challenges/fair-rations/problem

# High level solution for the below code:
# 0. If the sum of all elements in B is odd, return "NO" (because that means we can't make all elements even)
# 1. Iterate through each element in B
# 2. If the element is odd, increment it and the next element by 1
# 3. If the last element is odd, increment the second to last element by 1
# 4. Return the minimum number of loaves required

def fairRations(B):
    # Write your code here
    
    minRequired = 0
    
    if sum(B) % 2 != 0:
        return "NO"
    
    for num in range(len(B)):
        if B[num] % 2 != 0:
            B[num] += 1
            minRequired += 2
            if num == len(B) - 1:
                B[num - 1] += 1
            else:
                B[num+1] += 1
    return str(minRequired)
    