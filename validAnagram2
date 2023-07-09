class Solution:
    
    def validAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        """
        #put comments on each line of code
        # use a hashmap to store the frequency of each character
        hashmap = {}
        # iterate through the first string and store the frequency of each character
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        # iterate through the second string and decrement the frequency of each character
        for char in t:
            # if the character is not in the hashmap, return False
            if char in hashmap:
                # if the frequency of the character is 0, return False
                hashmap[char] -= 1
            else:
                return False
        # iterate through the hashmap and check if the frequency of each character is 0
        for key in hashmap:
            if hashmap[key] != 0:
                return False
        
        return True
    
sol = Solution()
print(sol.validAnagram("anagram", "nagaram"))
