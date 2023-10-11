# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # The main function to check if a tree is a valid BST.
        # It initializes the range of values to the widest possible (-infinity to infinity)
        # and delegates the validation to the helper function.
        return self.isBstUtil(root, float('-inf'), float('inf'))    
    
    def isBstUtil(self, root, min, max):
        """
        Recursive helper function to validate the BST.
        
        It works by narrowing down the valid range for node values at each level of recursion.
        
        :param root: The current root node.
        :param min: The minimum valid value for the current node.
        :param max: The maximum valid value for the current node.
        :return: True if it's a valid BST, False otherwise.
        """
        
        # Base case: if the node is None (i.e., we've reached a leaf), it's a valid BST.
        if root == None:
            return True
        
        # Check if the current node's value is within the specified range.
        # Then, for its left child, the maximum allowed value becomes the current node's value.
        # For its right child, the minimum allowed value becomes the current node's value.
        # Both these recursive calls must return True for the entire tree to be a valid BST.
        if (root.val > min and root.val < max 
            and self.isBstUtil(root.left, min, root.val) 
            and self.isBstUtil(root.right, root.val, max)):
            return True
        else:
            return False
