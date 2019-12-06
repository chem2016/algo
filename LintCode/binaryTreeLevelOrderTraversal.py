"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def __init__(self):
        pass

    def levelOrder(self, root):
        # write your code here
        queue = [root]
        retArr = []
        while(len(queue)):
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            retArr.append(level)
            
        return retArr

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

solution = Solution()
result = solution.levelOrder(tree)
print(result)