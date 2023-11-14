class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # 2 possible different soltuions
        # 1: Naive approach. Brute force
        # 2: create set or something similar

        #1)

        if len(nums) == 0 or len(nums) == 1:
            return False

        for num in range(len(nums)):
            for i in range(num+1, len(nums)):

                if nums[num] == nums[i]:
                    return True

        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashset = set()

        for num in nums:
            
            if num in hashset:
                return True
            
            hashset.add(num)

        return False
    
    