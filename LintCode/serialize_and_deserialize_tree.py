"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import collections

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def __init__(self):
        pass

    def serialize(self, root):
        # write your code here
        result_arr = []
        queue = collections.deque([root])
        while(queue):
            node = queue.popleft()
            if node is not None:
                result_arr.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result_arr.append('#')
        
        last_index = len(result_arr) - 1
        while(last_index):
            if result_arr[last_index] == "#":
                result_arr.pop(-1)
            else:
                break
            last_index -= 1

        return "{" + ','.join(result_arr) + "}"

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
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
        
solution = Solution()
result = solution.deserialize("{3,9,20,#,#,15,7}")
print(result.left.val)

string = solution.serialize(result)
print(string)