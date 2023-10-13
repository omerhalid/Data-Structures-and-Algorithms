#Maximum depth of binary tree
#Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

#Problem Statement:
#Given a binary tree, find its maximum depth.
#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#Note: A leaf is a node with no children.

#High Level Solution:
#Recursively traverse the tree and keep track of the depth, add 1 to the depth for each level because the root node is level 1
#Return the maximum depth

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0

        left_depth = self.maxDepth(root.left) + 1 #+1 for head node
        right_depth = self.maxDepth(root.right) + 1 #+1 for head node

        if left_depth > right_depth:
            return left_depth
        else:
            return right_depth
