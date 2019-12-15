import collections
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
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def __init__(self):
        pass
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []
        res = []
        stack = [(root, "")]
        
        while stack:
            node, strr = stack.pop()
        
            # [1->]
            # [1->] https://www.youtube.com/watch?v=Zr_7qq2f16k
            if not node.left and not node.right:
                res.append(strr + str(node.val))
            if node.left:
                stack.append((node.left, strr + str(node.val) + "->"))
            if node.right:
                stack.append((node.right, strr + str(node.val) + "->"))
            
        return res

def deserialize(data):
        # write your code here
        if data == "{}":
            return None
        data_arr = data[1:-1].split(',')
        queue = collections.deque([])
        root = TreeNode(data_arr[0])
        queue.append(root)
        is_left = True
        level = 0
        for i in range(1, len(data_arr)):
            if data_arr[i] != '#':
                node = TreeNode(data_arr[i])
                if is_left:
                    queue[level].left = node
                else:
                    queue[level].right = node
                queue.append(node)
            if not is_left:
                level += 1
                
            is_left = not is_left
        
        return root

#{1,2,3,#,5}
tree = deserialize("{1,2,3,#,5}")
solution = Solution()
result = solution.binaryTreePaths(tree)
print(result)