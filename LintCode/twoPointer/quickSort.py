class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        # quick sort
        self.quickSort(A, 0, len(A)-1)
        
    def quickSort(self, A, low, high):
        if low < high:
            border = self.partition(A, low, high)
            self.quickSort(A, low, border-1)
            self.quickSort(A, border+1, high)
    
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
A = [3, 2, 1, 4, 5]
solution.sortIntegers2(A)
print(A)