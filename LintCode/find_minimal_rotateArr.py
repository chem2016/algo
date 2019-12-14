class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1
        while(start + 1 < end):
            mid = (start + end) // 2
            if nums[mid] > nums[end]:    # compare with the end and check for an unrotate arr
                start = mid
            else:
                end = mid
                
        return nums[start] if nums[start] < nums[end] else nums[end]