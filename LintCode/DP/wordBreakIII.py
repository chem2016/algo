class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # Write your code here
        lower_dict = self.initialize(dict)
        lower_s = s.lower()
        
        # dp[i][j] = Sigma(k=i to j)dp[i][k]*dp[k+1][j]
        n = len(lower_s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i, n):
                if lower_s[i:j+1] in lower_dict:
                    dp[i][j] = 1
        
        for i in range(n):
            for j in range(i, n):
                for k in range(i, j):
                    dp[i][j] += dp[i][k]*dp[k+1][j]
                    
        return dp[0][-1]
        
        
    def initialize(self, dict):
        hash_set = set()
        for word in dict:
            hash_set.add(word.lower())
            
        return hash_set
