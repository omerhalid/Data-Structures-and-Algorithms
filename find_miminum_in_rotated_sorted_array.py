# Find minimum in rotated sorted array
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# High level solution for the below code:
# This code uses a binary search approach to find the minimum element in a rotated sorted array. 
# It takes advantage of the fact that a rotated sorted array has one sorted part and one part that's a sorted array starting from a 
# minimum element. It effectively reduces the search space by half in each iteration, resulting in a time complexity of O(log n).

class Solution:
    def findMin(self, nums):
        
        # nums.sort()
        # return nums[0]
        
        # Initialize the result with the first element of the array
        res = nums[0]
        
        # Initialize the left and right pointers
        l = 0
        r = len(nums) - 1
        
        # Continue the loop as long as the left pointer is less than or equal to the right pointer
        while l <= r:
            # If the element at the left pointer is less than the element at the right pointer,
            # it means the array from l to r is sorted (not rotated), so the minimum is nums[l]
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            # Calculate the middle index
            m = (l + r) // 2
            # Update the result with the minimum of the current result and the element at the middle index
            res = min(res, nums[m])
            # If the element at the middle index is greater than or equal to the element at the left pointer,
            # it means the array from l to m is sorted and the minimum is not in this part, so move l to m + 1
            if nums[m] >= nums[l]:
                l = m + 1
            # Otherwise, the array from m to r must be sorted and the minimum is not in this part, so move r to m - 1
            else:
                r = m - 1
                
        # Return the result, which holds the minimum element of the array
        return res