class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def __init__(self):
        pass

    def myPow(self, x, n):
        # write your code here
        if n == 0:
            return 1
        absN = abs(n)
        res = 1
        while (absN > 0):
            if absN % 2 != 0:
                res *= x
            absN /= 2
            x *= x
        if n < 0:
            return 1/res
        return res

solution = Solution()
result = solution.myPow(9.88023, 3)
print(result)