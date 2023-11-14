# Longest Repeating Character Replacement
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s, k):
        cout = {}  # Initialize a dictionary to count the frequency of each character
        res = 0  # Initialize the result, which is the length of the longest valid substring
        
        l = 0  # Initialize the left pointer of the sliding window
        maxf = 0  # Initialize the maximum frequency of any character within the current window
        
        for r in range(len(s)):  # Iterate over the string with the right pointer
            cout[s[r]] = cout.get(s[r], 0) + 1  # Increment the count of the current character
            maxf = max(maxf, cout[s[r]])  # Update the maximum frequency if necessary
            
            # If the size of the window minus the frequency of the most common character is greater than k
            while r - l + 1 - maxf > k:
                cout[s[l]] -= 1  # Decrement the count of the character at the left of the window
                l += 1  # Move the left pointer to the right
                
            res = max(res, r - l + 1)  # Update the result if the size of the current window is greater
            
        return res  # Return the length of the longest valid substring