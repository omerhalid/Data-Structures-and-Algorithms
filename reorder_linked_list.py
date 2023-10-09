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

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode):
        slow = head
        fast = head.next
        
        while fast != None and fast.next != None: # we want to stop at the middle of the linked list
            slow = slow.next #shift by 1 node
            fast = fast.next.next #shift by 2 nodes
        
        #Now slow is at the middle of the linked list
        second_half_head = slow.next #second half of the linked list
        slow.next = None #break the linked list into 2 halves
        prev = None #prev is the head of the reversed second half of the linked list
        
        #We want to reverse the second half of the linked list
        while second_half_head != None:
            tmp = second_half_head.next #store the next node of the second half of the linked list
            second_half_head.next = prev #reverse the second half of the linked list
            prev = second_half_head #shift prev by 1 node
            second_half_head = tmp #shift second_half_head by 1 node
            
        
        #merge the first half and the reversed second half
        first_half_head = head
        second_half_head = prev #prev is the head of the reversed second half of the linked list
        
        #continue until one of the linked lists is empty
        while second_half_head != None:
            temp1 = first_half_head.next #store the next node of the first half of the linked list
            temp2 = second_half_head.next #store the next node of the second half of the linked list
            
            first_half_head.next = second_half_head #merge the first half and the reversed second half
            second_half_head.next = temp1 #merge the first half and the reversed second half
            
            first_half_head = temp1 #shift first_half_head by 1 node
            second_half_head = temp2 #shift second_half_head by 1 node