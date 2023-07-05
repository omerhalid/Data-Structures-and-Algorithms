# Description: Given an array of integers, return indices of the two numbers such that they add up to a specific target.

class Solution:
    def twoSum(self, num, target):
        prevMap = {} # val : index
        
        for i, n in enumerate(num):
            diff = target - n
            
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return 
    
newSolution = Solution()
arr = [2, 7, 11, 15]
target = 13

print(newSolution.twoSum(arr, target))
