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

#High Level Solution for the below code:
#1. Create a list and Sort the array
#2. Iterate through the array using enumerate
#3. If the number is the same as the previous number, continue
#4. Set left pointer to index + 1
#5. Set right pointer to last index
#6. While left < right
#7. If the sum of the three numbers is less than 0, increment left pointer
#8. If the sum of the three numbers is greater than 0, decrement right pointer
#9. If the sum of the three numbers is equal to 0, append to result
#10. Increment left pointer
#11. While the left pointer is the same as the previous number, increment left pointer
#12. Return result

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
