"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    https://www.youtube.com/watch?v=LfKRZ_qCmYQ
    """
    def flatten(self, root):
        # write your code here
        if not root:
            return None
        self.pre = None
        self.dfs(root)
        return root
        
    def dfs(self, root):
        if not root:
            return None
        self.dfs(root.right)
        self.dfs(root.left)
        
        root.right = self.pre
        root.left = None
        self.pre = root
            