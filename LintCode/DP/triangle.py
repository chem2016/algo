class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        # f[i][j] = min(f[i-1][j], f[i-1][j-1]) + triangle[i][j]

        n = len(triangle)
        dp = [[0] * (i+1) for i in range(n)]
        dp[0][0] = triangle[0][0]

        # first colomn and last colomn in each row need to be initialized 
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]

        for i in range(2, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        
        return min(dp[n-1])

solution = Solution()
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
minimumTotal = solution.minimumTotal(triangle)
print(minimumTotal)