class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def __init__(self):
        pass

    def longestPalindrome(self, s):
        # write your code here
        if len(s) <= 1:
            return s
        else:
            longestSubstring = ""
            for i in range(0, len(s)):
                new_left, new_right = self.isPalindrome(s, i, i+1)
                if (new_right - new_left) > 0 and (new_right - new_left + 1) > len(longestSubstring):
                    longestSubstring = s[new_left: new_right+1]
                
                new_left, new_right = self.isPalindrome(s, i, i)
                if (new_right - new_left) > 0 and (new_right - new_left + 1) > len(longestSubstring):
                    longestSubstring = s[new_left: new_right+1]

            return longestSubstring
                    
    def isPalindrome(self, s, left, right):
        while(left >= 0 and right < len(s)):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        
        return left + 1, right - 1

solution = Solution()
result = solution.longestPalindrome('abcdzdca')
print(result)