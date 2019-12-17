class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    # def partitionArray(self, nums, k):
    #     # write your code here
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         while left < right and nums[left] < k:
    #             left += 1
    #         while left < right and nums[right] >= k:
    #             right -= 1
    #         if left < right:
    #             nums[left], nums[right] = nums[right], nums[left]
    #             left += 1
    #             right -= 1
                
    #     return left

    def partitionArray(self, nums, k):
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left

solution = Solution()
A = [7,7,9,8,6,6,8,7,9,8,6,6]
result = solution.partitionArray(A, 10)
print(result)