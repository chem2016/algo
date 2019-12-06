class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def __init__(self):
        pass

    def numIslands(self, grid):
        # write your code here
        visited = [[False for ele in row] for row in grid]
        islands = []
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if visited[i][j]:
                    continue
                self.traverse(i, j, grid, visited, islands)

        return islands

    def traverse(self, i, j, grid, visited, islands):

        island_size = 0
        queue = [[i, j]]
        while(len(queue)):
            node = queue.pop(0)
            i, j = node[0], node[1]
            if visited[i][j]:
                continue
            visited[i][j] = True
            if grid[i][j] == 0:
                continue
            island_size += 1
            neighbor_nodes = self.get_neighbor_nodes(node, grid, visited)
            for neighbor_node in neighbor_nodes:
                queue.append(neighbor_node)
        if island_size > 0:
            islands.append(island_size)

    def get_neighbor_nodes(self, node, grid, visited):
        neighbor_nodes = []
        i, j = node[:]
        if i > 0 and not visited[i-1][j]:
            neighbor_nodes.append([i-1, j])
        if i < len(grid) - 1 and not visited[i+1][j]:
            neighbor_nodes.append([i+1, j])
        if j > 0 and not visited[i][j-1]:
            neighbor_nodes.append([i, j-1])
        if j < len(grid[i]) - 1 and not visited[i][j+1]:
            neighbor_nodes.append([i, j+1])
        
        return neighbor_nodes

solution = Solution()
result = solution.numIslands([[1,1,0,0,0],[0,1,0,0,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,1]])
 
print(len(result))