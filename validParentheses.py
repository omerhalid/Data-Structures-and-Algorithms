class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        
        hasmap = {')':'(', ']':'[', '}':'{'}
        
        for char in s:
            if char in hasmap:
                if stack and stack[-1] == hasmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
                
        return True if not stack else False # if stack is empty, return True, else return False
