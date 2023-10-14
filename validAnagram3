class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s) == sorted(t)

        letter_dict1 = {}
        letter_dict2 = {}

        if len(s) != len(t):
            return False

        for letter in range(len(s)):

            if s[letter] not in letter_dict1:
                letter_dict1[s[letter]] = 0
            letter_dict1[s[letter]] += 1
            
            if t[letter] not in letter_dict2:
                letter_dict2[t[letter]] = 0
            letter_dict2[t[letter]] += 1

        if letter_dict1 == letter_dict2:
            return True
