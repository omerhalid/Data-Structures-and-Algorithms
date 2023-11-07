#Length of longest substring without repeating characters
#Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

#High level solution for the below problem:
#1. Use a set to store the characters
#2. Use a left pointer and a right pointer
#3. Move the right pointer until you find a duplicate character
#4. Move the left pointer until you remove the duplicate character
#5. Repeat steps 3 and 4 until the right pointer reaches the end of the string
#6. Return the length of the longest substring

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res