# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        results = []
        stack = []
        while (root or len(stack)):
            while root:
                stack.append(root)
                root = root.left
            current = stack.pop()
            results.append(current.val)
            current = current.right

        return results