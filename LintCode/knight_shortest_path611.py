import collections
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def __init__(self):
        pass

    def shortestPath(self, grid, source, destination):
        # write your code here
        delta_X = [1, 1, -1, -1, 2, 2, -2, -2]
        delta_Y = [2, -2, 2, -2, 1, -1, 1, -1]
        queue = collections.deque([(source.x, source.y)])
        distance = {(source.x, source.y): 0}    # use a dict to keep track of where you went and values

        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return distance[(x, y)]
            for dx, dy in zip(delta_X, delta_Y):
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in distance:
                    continue
                if self.isValid(next_x, next_y, grid):
                    distance[(next_x, next_y)] = distance[(x, y)] + 1
                    queue.append((next_x, next_y))
                else:
                    continue
        return -1  
            
    def isValid(self, x, y, grid):
        if x < len(grid) and x >= 0 and y < len(grid[0]) and y >= 0:
            if grid[x][y] != 1:
                return True
            else:
                return False
        else:
            return False
            
            
source = Point(0, 0)
destination = Point(7, 0)
# grid = [[0,0,0], [0,0,0], [0,0,0]]
# grid = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
grid = [[0,0,0,0,1,1],[1,0,1,0,0,1],[0,0,1,0,0,1],[0,0,1,1,0,1],[1,0,1,0,0,1],[0,0,1,0,0,1],[0,0,1,0,0,1],[0,0,1,0,0,1]]

solution = Solution()
result = solution.shortestPath(grid, source, destination)
print(result)