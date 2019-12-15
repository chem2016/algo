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
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        self.arr = []
        self.dfs(root)
        return self.arr[k-1]
        
    def dfs(self, root):
        
        if root:
            self.dfs(root.left)
            self.arr.append(root.val)
            self.dfs(root.right)