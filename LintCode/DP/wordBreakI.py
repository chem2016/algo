class Solution:
    """
    107. Word Break
    中文English
    Given a string s and a dictionary of words dict, determine if s can be broken into a space-separated sequence of one or more dictionary words.

    Example
    Example 1:
        Input:  "lintcode", ["lint", "code"]
        Output:  true

    Example 2:
	Input: "a", ["a"]
	Output:  true
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    class Solution:
    
        def wordBreak(self, s, dict):
            # write your code here
            # abcdefgh
            #   i-j  i
            if len(dict) == 0:
                return len(s) == 0
            
            n = len(s)
            f = [False] * (n+1)
            f[0] = True
            maxLength = max([len(word) for word in dict])
            
            for i in range(1, n+1):
                for j in range(1, min(maxLength, i)+1):
                    if not f[i-j]:
                        continue
                    if s[i-j:i] in dict:
                        f[i] = True
                        break
                    
            return f[n]