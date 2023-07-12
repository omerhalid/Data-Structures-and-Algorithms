class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        counter = 0
        left, right = 0, 1
        
        while right < len(nums):
                
            if nums[left] == nums[right]:
                nums.pop(right)
                right = left + 1
            else:
                counter += 1
                left = right
                right += 1
            
        print(nums)

        return counter

sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums))