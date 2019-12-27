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
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        # write your code here
        if root == None:
            return None
        if p.left != None:
            # go to left substree and return the rightmost child
            temp = p.left
            while(temp.right):
                temp = temp.right
            return temp
        else:
            # search p in root and the node from which we take the last right turn is the answer
            store = None
            while(p.val != root.val):
                if p.val > root.val:
                    store = root
                    root = root.right
                else:
                    root = root.left
            return store