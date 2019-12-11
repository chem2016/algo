class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if len(nums) == 1:
            return nums[0]
        start, end = 0, len(nums)-1
        
        while(start + 1 < end):
            mid = (start + end) // 2
            if nums[mid+1] > nums[mid]:
                start = mid
            else:
                end = mid
        
        if nums[start] > nums[end]:
            return nums[start]
        else:
            return nums[end]
