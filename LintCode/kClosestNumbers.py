class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def __init__(self):
        pass

    def kClosestNumbers(self, A, target, k):
        # write your code here
        if k > len(A):
            return -1
        if k == 0:
            return []
        mostClosestNumber = self.binarySearch(A, target)
        print("mostClosestNumber: ", mostClosestNumber) 
        retArr = [A[mostClosestNumber]]
        left = mostClosestNumber - 1
        right = mostClosestNumber + 1

        while len(retArr) < k:
            if self.leftIsCloser(A, left, right, target):
                retArr.append(A[left])
                left -= 1
            else:
                retArr.append(A[right])
                right += 1

        return retArr
    
    def binarySearch(self, A, target):
        """
        @return: index of the closet element in arr
        """
        start, end = 0, len(A) - 1

        while(start + 1 < end):
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                end = mid

        if abs(A[start] - target) <= abs(A[end] - target):
            return start
        else:
            return end

    def leftIsCloser(self, A, left, right, target):
        """
        @return: true if A[left] is smaller
        """
        if left < 0:
            return False
        if right > len(A) - 1:
            return True
        if abs(A[left] - target) <= abs(A[right] - target):
            return True
        else:
            return False

solution = Solution()
result = solution.kClosestNumbers([1,4,8,12,16,28,38], 38, 4)
print(result)