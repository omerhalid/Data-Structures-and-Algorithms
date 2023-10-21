#Remove Nth From the end of a linked list
#Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

#Problem statement:
#Given the head of a linked list, remove the nth node from the end of the list and return its head.

#High level solution with calculating length:
#Calculate the length of the list
#If n is out of bounds, return head
#If the node to delete is the head, return head.next
#Find the length-n-1 node from the beginning
#Delete the nth node, if it exists (temp.next = temp.next.next)
#return head

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #length - n - 1

        # Calculate the length
        length = 0
        temp = head
        while temp != None:
            length += 1
            temp = temp.next

        # If n is out of bounds
        if n > length:
            return head

        # If the node to delete is the head
        if n == length:
            return head.next

        # Find the n-1 node from the beginning
        temp = head
        for i in range(length - n - 1):
            temp = temp.next

        # Delete the nth node
        if temp.next:
            temp.next = temp.next.next

        return head
