#Kth smallest element in BST
#Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

#Problem Statement:
#Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

#High Level Solution (iterative):
#Use inorder traversal to get the elements in ascending order
#Return the kth element

"""
Step-by-step guide to solving the "kth Smallest Element in a BST" problem using iterative in-order traversal:

1. Initialize:
    - Set a counter `n` to 0 for keeping track of visited elements.
    - Create an empty `stack` for in-order traversal.
    - Start with the `current` node set to the BST's root.

2. Traverse to the Leftmost Node:
    - As long as `current` is not null, push it onto the `stack` and move `current` to its left child. 
      There will be two while loops nested in this step. (while current is not null or while stack is not empty)
                                                            and while current is not null)
      This step ensures we first visit the smallest values.

3. Process the Current Node:
    - Pop a node from the `stack` and make it the `current` node.
    - Increment your counter `n`.
    - If `n` equals `k`, you've found your kth smallest. Return the value of the current node.

4. Move to Right Child:
    - Update `current` to its right child.
      This step ensures that after processing a node, you move on to the next bigger value in the BST.

5. Repeat:
    - Continue the process until `n` equals `k` or until you've traversed all nodes (i.e., when both 
      the `stack` is empty and `current` is null).

Note: The in-order traversal of a BST visits nodes in ascending order. The iterative approach uses 
a stack to explicitly track nodes, avoiding the overhead of recursive function calls.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        #in order traversal (dfs)
        #left - root - right

        n = 0
        stack = []

        current = root

        while current != None or stack: #while current is not null and stack is not empty
            while current != None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            n += 1

            if n == k:
                return current.val

            current = current.right

