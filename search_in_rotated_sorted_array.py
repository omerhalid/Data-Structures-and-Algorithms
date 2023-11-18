#Search in rotated sorted array
#Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

# Example

# Let's consider nums = [4,5,6,7,0,1,2] and target = 0:

#     Initially, l = 0, r = 6, and mid = 3.
#     nums[mid] = 7 which is not equal to target.
#     The left portion [4,5,6,7] is sorted, but target is not in this range.
#     Hence, l is moved to mid + 1.
#     In the next iterations, the algorithm will narrow down to the sorted portion containing the target.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # super similar to find minimum in rotated sorted array

        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

             # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1