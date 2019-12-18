class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        left, right = 0, len(nums) - 1
        targetK = len(nums) - n + 1
        while(left <= right):
            pos = self.partition(nums, left, right)
            if targetK == pos + 1:
                return nums[pos]
            elif targetK < pos + 1:
                right = pos - 1
            else:
                left = pos + 1
        return 0
        
    def partition(self, A, low, high):
        pivot = self.get_pivot(A, low, high)
        pivot_value = A[pivot]
        
        A[pivot], A[low] = A[low], A[pivot]
        border = low
        
        for i in range(low, high+1):
            if A[i] < pivot_value:
                border += 1
                A[i], A[border] = A[border], A[i]
        A[low], A[border] = A[border], A[low]
        
        return border
        
    def get_pivot(self, A, low, high):
        # get medium among low, high, middle
        mid = (low + high) // 2
        pivot = high
        if A[low] < A[mid]:
            if A[mid] < A[high]:
                pivot = mid
        if A[low] < A[mid]:
            if A[mid] < A[high]:
                pivot = mid
        elif A[low] < A[high]:
            pivot = low

        return pivot

solution = Solution()
result = solution.kthLargestElement(1, [1,3,4,2])
print(result)