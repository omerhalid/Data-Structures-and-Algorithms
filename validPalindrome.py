# Valid Palindrome
# Link: https://leetcode.com/problems/valid-palindrome/

# High level solution for the below problem:
# 1. Create a new string with only alphanumeric characters. Use isalnum() method
# 2. Compare the new string with its reverse
# 3. If they are equal, return True
# 4. Else, return False



class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        new_str = ""
        
        for i in s:
            if i.isalnum():
                new_str += i.lower()
            else:
                continue
        return new_str == new_str[::-1]
    
sol = Solution()
print(sol.isPalindrome("amanaplanacanalpanama"))