#3 sum
#Link: https://leetcode.com/problems/3sum/

#Problem Statement:
#Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
#Find all unique triplets in the array which gives the sum of zero.
#Note:
#The solution set must not contain duplicate triplets.
#Example:
#Given array nums = [-1, 0, 1, 2, -1, -4],
#A solution set is:
#[
#  [-1, 0, 1],
#  [-1, -1, 2]
#]

#Time Complexity: O(n^2)
#Space Complexity: O(n)

#High Level Solution:
#Sort the array
#For each element in the array, use two pointers to find the other two elements that sum to 0
#If the sum is 0, add the three elements to the result list
#If the sum is greater than 0, decrement the second pointer
#If the sum is less than 0, increment the first pointer

#Solution:

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        nums.sort()

        for index, num in enumerate(nums):
            if index > 0 and num == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                threeSum = num + nums[left] + nums[right]

                if threeSum < 0:
                    left += 1
                    
                elif threeSum > 0:
                    right -= 1

                elif threeSum == 0:
                    result.append([num, nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left - 1] and left < right: #skip duplicates
                        left += 1
        
        return result
