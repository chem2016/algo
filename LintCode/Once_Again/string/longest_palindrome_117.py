class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        ans = 0
        hashTable = {}
        for char in s:
            if char in hashTable:
                hashTable[char] += 1
            else:
                hashTable[char] = 1
        # {a: 1, b: 1, c: 4, d: 2}
        print(hashTable)
        hasOdd = False
        for key, value in hashTable.items():
            if value % 2 == 0:
                ans += value
            else:
                hasOdd = True
                ans += (value - 1)
        
        if hasOdd:
            return ans + 1
        return ans

solution = Solution()
result = solution.longestPalindrome('abccccdd')
print(result)