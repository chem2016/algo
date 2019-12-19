class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        self.results = []
        # keep track of visited positions
        visited = {
            'col': set(),
            'sum': set(),
            'diff': set()
        }
        
        self.dfs([], visited, n)
        
        return self.results
        
    def dfs(self, permutation, visited, n):
        if len(permutation) == n:
            self.results.append(self.draw(permutation))
            return
        
        row = len(permutation) # only record col number since one row one number
        
        for col in range(n):
            if not self.isValid(permutation, col, visited):
                continue
            permutation.append(col)
            visited['col'].add(col)
            visited['sum'].add(row + col)
            visited['diff'].add(row - col)
            self.dfs(permutation, visited, n)
            visited['col'].remove(col)
            visited['sum'].remove(row + col)
            visited['diff'].remove(row - col)
            permutation.pop()
            
    def isValid(self, permutation, col, visited):
        # check if a (row col) has been occupied
        row = len(permutation)
        if col in visited['col']:
            return False
        if row + col in visited['sum']:
            return False
        if row - col in visited['diff']:
            return False
        return True
            
    def draw(self, permutation):
        # an example of permutation: [1, 3, 0, 2]
        # convert this to [".Q..", etc..]
        board = []
        n = len(permutation)
        for col in permutation:
            row_string = ''.join(['Q' if c == col else '.' for c in range(n)])
            board.append(row_string)
            
        return board