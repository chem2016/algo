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
    @return: True if this Binary tree is Balanced, or false.
    https://www.youtube.com/watch?v=SH3qzLmLoS0
    """
    def isBalanced(self, root):
        if self.getHeight(root) != -1:
            return True
        else:
            return False
        
    def getHeight(self, root):
        if root is None:
            return 0
        leftHeight, rightHeight = self.getHeight(root.left), self.getHeight(root.right)
        if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1