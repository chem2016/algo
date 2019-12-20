class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if nums is None:
            return []
        if len(nums) <= 1:
            return [nums]
            
        self.results = []
        visited = set() # need to keep track which number has already added to the current permutation
        self.dfs([], nums, visited) # different than subsets, here you do not need index, because it always start from 0.
        
        return self.results
        
    def dfs(self, permutation, nums, visited):
        
        if len(permutation) == len(nums):
            self.results.append(list(permutation))
        
        preNum = nums[0] - 1
        for i in range(0, len(nums)):
            if not i in visited and nums[i] != preNum:  # since num is not unique, so in the set we check index, not num[i]
                preNum = nums[i]  # we do not dfs the same number
                permutation.append(nums[i])
                visited.add(i)
                self.dfs(permutation, nums, visited)
                visited.remove(i)
                permutation.pop()


solution = Solution()
result = solution.permute([1,1,2])
print(result)