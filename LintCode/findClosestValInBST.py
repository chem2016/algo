"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        lower, upper = root, root
        
        while root:
            if target < root.val:
                upper = root
                root = root.left
            elif target > root.val:
                lower = root
                root = root.right
            else:
                return root.val
                
        if abs(lower.val - target) < abs(upper.val - target):
            return lower.val
        return upper.val