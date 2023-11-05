#Longest consecutive sequence
#Link: https://leetcode.com/problems/longest-consecutive-sequence/

#High level solution for the below code:
# 1. Create a set of the input array. Why set? Because we want to check if a number is in the array in O(1) time
# 2. Initialize a counter variable to 0
# 3. Initialize a longest_counter variable to 0 => this will be the final answer
# 4. Iterate through the set
# 5. If the current number - 1 is not in the set, then the current number is the starting point of a sequence
# 6. Initialize a current_num variable to the current number, current num is the starting point of the sequence
# 7. Initialize a counter variable to 1 => we have seen one number so far
# 8. While the current_num + 1 is in the set, increment the counter and increment the current_num
# 9. Update the longest_counter variable to the max of the longest_counter and counter => this is the final answer
# 10. Return the longest_counter variable


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        num_set = set(nums)

        counter = 0
        longest_counter = 0

        for num in num_set:

            if num - 1 not in num_set: #so the num is the starting point of a sequence

                current_num = num
                counter = 1

                while current_num + 1 in num_set:

                    counter += 1
                    current_num += 1 #shift the current num

                longest_counter = max(longest_counter, counter)

        return longest_counter





                