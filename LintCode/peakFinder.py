class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        # look at if it is at the ascending part, 
        # if so set start to mid, 
        # if it is at decsending part, set end =mid
        # gradually getting close to peak by moving left and right
        start, end = 1, len(A) - 2
        while (start + 1 < end):
            mid = (start + end) // 2
            if A[mid] < A[mid + 1]:   
                start = mid
            else:
                end = mid
                
        if A[start] > A[end]:
            return start
        else:
            return end