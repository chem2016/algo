class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        # write your code here
        testArr = teststr.split(' ')
        if len(pattern) != len(testArr):
            return False
            
        wordDict = {}
        hashValue = {}
        
        for char, word in zip(pattern, testArr):
            if char in wordDict:
                if wordDict[char] != word:
                    return False
            else:
                if word in hashValue:
                    return False
                else:
                    wordDict[char] = word
                    hashValue[word] = True   # take care of case like "dog dog dog dog"
        
        return True

solution = Solution()
result = solution.wordPattern('abba', 'dog cat cat dog')
print(result)