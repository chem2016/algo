class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def __init__(self):
        pass
    def deduplication(self, nums):
        # write your code here
        # [1,3,1,4,4,2]
        nums_set = set()
        for ele in nums:
            nums_set.add(ele)
        for i, ele in zip(range(len(nums_set)), nums_set):
            nums[i] = ele
        print(nums)

        return len(nums_set)

solution = Solution()
result = solution.deduplication([1,3,1,4,4,2])
print(result)
