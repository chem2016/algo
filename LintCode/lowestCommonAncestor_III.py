"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    https://www.youtube.com/watch?v=ACnM-YR6CjQ
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        Aexist, Bexist, lca = self.helper(root, A, B)
        if Aexist and Bexist:
            return lca
        else:
            None
        
    def helper(self, root, A, B):
        if not root:
            return False, False, None
        
        ALeftExist, BLeftExist, Leftlca = self.helper(root.left, A, B)
        ARightExist, BRightExist, Rightlca = self.helper(root.right, A, B)
        lca = None
        
        Aexist = ARightExist or ALeftExist or A == root
        Bexist = BRightExist or BLeftExist or B == root
        
        if A == root or B == root:
            lca = root
        elif Leftlca and Rightlca:
            lca = root
        elif not Leftlca and Rightlca:
            lca = Rightlca
        elif not Rightlca and Leftlca:
            lca = Leftlca
            
        return Aexist, Bexist, lca