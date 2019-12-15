"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        self.targetNode = None
        self.minimumValue = sys.maxsize
        self.helper(root)
        
        return self.targetNode
        
    def helper(self, root):
        
        if not root:
            return 0
        
        leftSum = self.helper(root.left)
        rightSum = self.helper(root.right)
        
        TotalSum = leftSum + rightSum + root.val
        
        if TotalSum < self.minimumValue:
            self.minimumValue = TotalSum
            self.targetNode = root
            
        return TotalSum