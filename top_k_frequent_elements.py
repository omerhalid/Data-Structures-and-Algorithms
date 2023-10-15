#Top K frequent elements
#Link: https://leetcode.com/problems/top-k-frequent-elements/

#Problem Statement:
#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

#We wil use Bucket Sort to solve this problem
#What is Bucket Sort? Bucket sort is mainly useful when input is uniformly distributed over a range.

#High Level Solution:
#Use a dictionary to store the frequency of each element in nums
#Use bucket sort to sort the elements by frequency. The elements in bucket are stored in ascending order by frequency. 

"""
    Initialize Data Structures:
        Initialize a list freq containing sub-lists. This will act as our bucket for sorting numbers based on their frequencies. The length of the list is len(nums) + 1 to account for frequencies ranging from 1 to the length of nums.
        Initialize a dictionary count that will store the frequency of each number in nums.
        Initialize a list result to store the final k frequent elements.

    Count Frequencies:
        Iterate over each number n in nums.
        For each number, if it's already a key in the count dictionary, increment its value. Otherwise, set its value to 1. This step populates the count dictionary with frequencies of each number.

    Populate the Buckets:
        For each key-value pair (i.e., element, frequency) in the count dictionary:
            Append the element to the sub-list at index frequency of freq. This groups elements in freq based on their frequencies.

    Extract Top k Frequent Elements:
        Iterate over the freq list in reverse (starting from the highest possible frequency to the lowest).
        For each sublist in freq:
            Iterate over each element in the sublist.
            Append the element to result.
            Check if the length of result has reached k. If it has, return result as the final answer.

By following this step-by-step guide, the top k frequent elements are effectively extracted without explicitly sorting all the elements, making it more efficient than straightforward sorting methods.
"""

class Solution:
    def topKFrequent(self, nums, k):
        
        count = {} #dictionary to store the frequency of each element in nums
        freq = [[] for i in range(len(nums) + 1)] #list to store the elements in nums by frequency. Why len(nums) + 1? Because the maximum frequency of an element in nums is len(nums)
        
        for n in nums:
            count[n] = count.get(n, 0) + 1 #store the frequency of each element in nums. If the element is not in count, set its frequency to 0 and add 1 to it. If the element is in count, add 1 to its frequency.
            
        for n, c in count.items(): #store the elements in nums by frequency. Iterate through count and store the element and its frequency in n and c respectively
            freq[c].append(n) #append the element to freq at the index equal to its frequency
            #what is n? n is the element in nums
            #what is c? c is the frequency of n
            
        res = [] #list to store the k most frequent elements
        for i in range(len(freq) - 1, 0, -1): #iterate through freq in reverse order
            for n in freq[i]: #iterate through the elements in freq
                res.append(n) #append the element to res
                if len(res) == k: #if the length of res is equal to k, return res
                    return res #return res
                
#time complexity: O(n)
#space complexity: O(n)
