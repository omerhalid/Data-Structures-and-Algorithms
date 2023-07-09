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