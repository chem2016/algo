class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if candidates == None:
            return []
        if len(candidates) == 0:
            return []

        self.result = []
        self.dfs(0, [], candidates, target)
        
        return self.result
        
    def dfs(self, staring_index, combination, candidates, target):
        if target < 0:
            return
        if target == 0:
            self.result.append(list(combination))
            
        for i in range(staring_index, len(candidates)):
            combination.append(candidates[i])
            self.dfs(i, combination, candidates, target - candidates[i])
            combination.pop()