# Invert binary tree
# Link: https://leetcode.com/problems/invert-binary-tree/

# DFS with recursion

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        
        #swap the left and right nodes
        temp = root.left
        root.left = root.right
        root.right = temp
        
        #recursively call the function on the left and right nodes
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root