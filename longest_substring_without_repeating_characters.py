# Longest substring without repeating characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #sliding window

        left = 0
        right = 0

        counter = 0

        hashset = set()

        while right < len(s):
            if s[right] not in hashset:
                hashset.add(s[right])
                right += 1
                counter = max(counter, right - left)

            else:
                hashset.remove(s[left])
                left += 1


        return counter