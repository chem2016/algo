class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]

        nums.sort()
        self.result = []
        self.dfs(0, nums, [])

        return self.result

    def dfs(self, index, nums, subset):
       self.result.append(subset[:])
       
       for i in range(index, len(nums)):
           if i != index and nums[i] == nums[i-1]: # this line is for subset II, otherwise code for subset I
               continue
           subset.append(nums[i])
           self.dfs(i+1, nums, subset)
           subset.pop() 

solution = Solution()
result = solution.subsetsWithDup([])
print(result)