class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def __init__(self):
        pass
    def moveZeroes(self, nums):
        # write your code here
        if len(nums) <= 1:
            return nums
        left, right = 0, 1
        while(right < len(nums) and left < len(nums)-1):
            leftNum, rightNum = nums[left], nums[right]
            if leftNum == 0 and rightNum != 0:
                self.swap(left, right, nums)
                left += 1
                right += 1
            elif leftNum == 0 and rightNum == 0:
                right += 1
            elif leftNum != 0 and rightNum == 0:
                left += 1
                right += 1
            else:
                left += 1
                right += 1
        
        return nums
        
    def swap(self, left, right, nums):
        
        tmp = nums[right]
        nums[right] = nums[left]
        nums[left] = tmp

solution = Solution()
result = solution.moveZeroes([0, 1, 0, 3, 12])
print(result)