class Solutiob:
    #itereative solution
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev, curr = None, head
        
        #Time complexity: O(n)
        #Space complexity: O(1)
        while curr:
            # save the next node
            nxt = curr.next
            # reverse the current node
            curr.next = prev
            # update the previous node
            prev=curr
            # move the pointers
            curr = nxt
        # return the new head
        return prev