#Reorder the given linked list, by taking the first element, then the last, then the second, then the second last, and so on until the end.
#Link: https://leetcode.com/problems/reorder-list/

#High level solution
#1. Find the middle of the linked list
#2. Reverse the second half of the linked list
#3. Merge the first half and the reversed second half
#4. Return the merged linked list

#Time complexity: O(n)
#Space complexity: O(1)
#2 pointers: slow and fast

#We can do this without using an array.
#We can reverse the second half of the linked list in place.

#How do we know when we've reached the middle of the linked list?
#When the fast pointer reaches the end of the linked list, the slow pointer is at the middle of the linked list.
#Slow pointer shifts by 1 node, fast pointer shifts by 2 nodes.

#If its an even number of nodes, the slow pointer will be at the first node of the second half of the linked list.
#If its an odd number of nodes, the slow pointer will be at the middle node of the linked list. 
#In odd number of nodes case, it doesnt matter if the second half of the linked list is longer than the first half of the linked list.

#Example input and output:
#Input: 1->2->3->4->5->NULL
#Output: 1->5->2->4->3->NULL

#First pointer: 1
#last pointer: 5

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode):
        
        # we will use fast and slow pointer to find the middle of the linked list

        #it is the combination of reversing a list and merging two lists

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next # shift by 2

        second = slow.next
        slow.next = None
        prev = None # prev is the head of the reversed second half of the linked list

        #reversing the second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        #merge the first half and the reversed second half

        first = head
        second = prev

        while second:
            temp1 = first.next # store the links because we will breake it
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1 # shift the first head by 1 node
            second = temp2 # shift the second head by 1 node