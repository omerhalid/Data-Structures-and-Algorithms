#Valid parentheses
#Link to problem: https://leetcode.com/problems/valid-parentheses/

#Problem description:
#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

#High level solution with stack:
#1. Create a stack
#2. Iterate through the string
#3. If the character is an opening bracket, push it onto the stack
#4. If the character is a closing bracket, pop the stack and check if the popped element is the corresponding opening bracket
#5. If it is not, return False
#6. If the stack is empty after iterating through the string, return True

#Time complexity: O(n)
#Space complexity: O(n)


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        for char in s:
          
            if char == '(' or char == '{' or char == '[':

                stack.append(char)
            
            else:

                if not stack:
                    return False
        
                if char == '}' or char == ']' or char == ')':

                    if stack[-1] == '(' and char == ')':
                        stack.pop()
                    elif stack[-1] == '[' and char == ']':
                        stack.pop()
                    elif stack[-1] == '{' and char == '}':
                        stack.pop()
                    else:
                        return False
            
        if not stack:
            return True

                

