import collections
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node

    find out the points
    copy all the points, save all the relations
    find all the edges, and save every edge
    """
    def __init__(self):
        pass

    def cloneGraph(self, node):
        # write your code here
        if node is None:
            return node
        root = node
        nodes = self.BFS(root)
        mapping = {} 
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

    def BFS(self, node):
        queue = collections.deque([node])
        result = set([node])
        while queue:
            currentNode = queue.popleft()
            for neighbor in currentNode.neighbors:
                if neighbor in result:
                    continue
                else:
                    result.add(neighbor)
                    queue.append(neighbor)

        return result  

node1 = UndirectedGraphNode(1)
node2 = UndirectedGraphNode(2)
node4 = UndirectedGraphNode(4)   
node1.neighbors.append(node2)
node1.neighbors.append(node4)
node2.neighbors.append(node1)
node2.neighbors.append(node4)
node4.neighbors.append(node1)
node4.neighbors.append(node2)

solution = Solution()
result = solution.cloneGraph(node1)

print(result.neighbors)
