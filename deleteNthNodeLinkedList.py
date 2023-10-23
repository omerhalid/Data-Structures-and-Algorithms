#Delete nth node in a linked list
#www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem

#Problem statement:
#You’re given the pointer to the head node of a linked list and the position of a node to delete.
#Delete the node at the given position and return the head node.
#A position of 0 indicates head, a position of 1 indicates one node away from the head and so on.
#The list may become empty after you delete the node.

#High level solution:
#1. If the list is empty, return None.
#2. If the position is 0, return the head’s next node.
#3. Create a temp node and set it to the head.
#4. Loop through the list until you reach the position (position - 1)
#5. Set the temp node to the next node
#6. Set toBeDeleted to the temp.next
#7. Set aft to toBeDeleted.next
#8. Set temp.next to aft
#9. Return the head node


# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(llist, position):
    # Write your code here
    
    if position == 0:
        return llist.next
    
    temp = llist
    
    for node in range(position-1):
        temp = temp.next
    
    toBeDeleted = temp.next
    
    aft = toBeDeleted.next
    
    temp.next = aft
    
    return llist
