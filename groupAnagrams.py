#Group anagrams 
#Link: https://leetcode.com/problems/group-anagrams/

# Anagram: Two words are anagrams if they have the same letters in different order

#Time Complexity: O(m*n) where m is the number of words and n is the length of the longest word

#We will use hash table to store the words and their anagrams

# lets say a = 80 -> 0, 80-80 = 0
# lets say b = 81 -> 1, 81-80 = 1
# lets say c = 82 -> 2, 82-80 = 2

# The idea is ord() function returns the unicode of the character and we subtract the unicode of 'a' from it to get the index of the character in the list

#Problem: The problem is about grouping words that are anagrams. An anagram is when you rearrange the letters of a word and form another word. For example, "act" and "cat" are anagrams.

#Solution Approach:
#The primary idea here is to represent each word by a unique signature that remains the same for all its anagrams. Imagine if all anagrams had the same "ID card" – then it's easy to group them together!

#How do we create this "ID card" or signature?:
#For every word, the solution calculates the frequency of each letter in the word and uses that as a unique identifier.

#For example, the word "aabbcc" would be represented as:
#2 times 'a', 2 times 'b', 2 times 'c' and 0 times every other letter.
#So its "ID card" would look something like: [2, 2, 2, 0, 0, ...] (with 26 total numbers, one for each letter of the alphabet).

def groupAnagrams(strs):
    anagrams = {}
    for word in strs:#for each word in the list
        key = [0]*26 #26 letters in the alphabet. Why do we have 26 zeros? Because we are going to count the number of times each letter appears in the word and store it in the key list
        for char in word: #count the number of times each letter appears in the word
            key[ord(char) - ord('a')] += 1 #this line does the counting and stores the count in the key list
        key = tuple(key) #convert the key list to a tuple
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    return anagrams.values() #we return the values not the keys in the dict
