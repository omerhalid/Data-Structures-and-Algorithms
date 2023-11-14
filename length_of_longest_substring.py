#Length of longest substring without repeating characters
#Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/


#  function lengthOfLongestSubstring(s)
#     Initialize a set 'windowChars' to keep track of the characters in the current window
#     Initialize 'left' to 0 (start of the current window)
#     Initialize 'maxLength' to 0 (length of the longest substring found so far)
#     Initialize 'right' to 0 (end of the current window)

#     while right is less than the length of s
#         if s[right] is not in 'windowChars'
#             Add s[right] to 'windowChars'
#             Increment 'right' by 1
#             'maxLength' = max('maxLength', 'right' - 'left')
#         else
#             Remove s[left] from 'windowChars'
#             Increment 'left' by 1

#     return 'maxLength'


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