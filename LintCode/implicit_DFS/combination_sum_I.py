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
        self.dfs(0, [], sorted(list(set(candidates))), target) # remove duplicates and sorted
        
        return self.result
        
    def dfs(self, staring_index, combination, candidates, target):
        if target < 0:
            return
        if target == 0:
            return self.result.append(list(combination))
            
        for i in range(staring_index, len(candidates)):
            combination.append(candidates[i])
            self.dfs(i, combination, candidates, target - candidates[i]) # instead of using i+1 here use i, so we can have one element using multiple times
            combination.pop()