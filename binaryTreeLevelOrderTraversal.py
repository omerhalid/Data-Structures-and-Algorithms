    # Edge Case Handling
    #     Check if root is None. If yes, return an empty list.

    # Initialization
    #     Create an empty list result to store the final answer.
    #     Initialize a queue with the root node of the tree.

    # BFS (Breadth-First Search) Iteration
    #     While there are nodes in the queue (ensuring all nodes are processed):
    #         Initialize an empty list current_level to store values of the nodes at the current level.
    #         Determine the number of nodes at the current level with level_size = len(queue).
    #         For each node in the current level (iterate level_size times):
    #             Dequeue the next node with current = queue.popleft().
    #             Add its value to current_level.
    #             If the node has a left child, enqueue the left child.
    #             If the node has a right child, enqueue the right child.
    #         If current_level is not empty, append it to result.

    # Return Result
    #     Finally, return the result list containing the level order traversal.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []

        result = []

        queue = deque([root])

        while(queue):

            current_level = []

            level_size = len(queue)

            for i in range(level_size): 

                current = queue.popleft()
                current_level.append(current.val)

                if current.left != None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)
            
            if current_level:
                result.append(current_level)
        
        return result