class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def __init__(self):
        pass
    def strStr(self, source, target):
        # Write your code here
        if len(target) > len(source):
            return -1
        else:
            for i in range(0, len(source) - len(target) + 1):
                if target == source[i:i+len(target)]:
                    return i
                    
            return -1

solution = Solution()
result = solution.strStr("abcdeft", 'bc')
print(result)