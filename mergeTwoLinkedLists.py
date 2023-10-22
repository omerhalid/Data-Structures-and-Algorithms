#Merge two sorted linked lists
#Link: https://leetcode.com/problems/merge-two-sorted-lists/

#Problem statement:
#Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

#High level solution:
#Initialize a dummy node and current == dummy
#While both lists are not empty
#If l1.val < l2.val, current.next = l1, l1 = l1.next
#Else, current.next = l2, l2 = l2.next
#current = current.next
#If l1 is not empty, current.next = l1
#Else, current.next = l2
#return dummy.next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Initialize dummy and current pointers
        dummy = ListNode(0)
        current = dummy

        # While neither of the lists is empty
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            # Move to the next node in the merged list
            current = current.next

        # At the end of the loop, one of list1 and list2 can still have nodes.
        # Since the lists are already sorted, we just link the non-empty list to the end of the merged list.
        if list1 is not None:
            current.next = list1
        else:
            current.next = list2

        # The merged list starts from the next of the dummy node
        return dummy.next

