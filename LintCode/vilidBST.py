"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    https://www.youtube.com/watch?v=ewrpOMA6LrY
    """
    def isValidBST(self, root):
        # write your code here
        
        return self.valid(root, float('-inf'), float('inf'))
        
    def valid(self, root, minimum, maximum):
        
        if root is None:
            return True
            
        if root.val <= minimum or root.val >= maximum:
            return False
        
        return self.valid(root.left, minimum, root.val) and self.valid(root.right, root.val, maximum)
        