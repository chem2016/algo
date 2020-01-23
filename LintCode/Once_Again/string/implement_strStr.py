class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        n = len(target)
        prefix = [0]*n
        self.prefixTable(prefix, target, n)
        self.movePrefixTable(prefix, n)
        print(prefix)
        # KMP search
        m = len(source) # pointer i
        i, j = 0, 0
        while(i < m):
            if j == n-1 and source[i] == target[j]:
                print "Found pattern at index " + str(i-j) 
                return i-j
            if source[i] == target[j]:
                i += 1
                j += 1
            else:
                j = prefix[j]
                if j == -1:
                    i += 1
                    j += 1
        return -1
    
    def prefixTable(self, prefix, pattern, n):
        prefix[0]
        length = 0
        i = 1
        while(i < n):
            if pattern[i] == pattern[length]:
                length += 1
                prefix[i] = length
                i += 1
            else:
                if length > 0:
                    length = prefix[length-1]
                else:
                    prefix[i] = length
                    i += 1

    def movePrefixTable(self, prefix, n):
        for i in range(1, n, -1):
            prefix[i] = prefix[i-1]
        prefix[0] = -1
    
solution = Solution()
# pattern = 'target'
# prefix = [0]*6
# solution.prefixTable(prefix, pattern, 6)
# solution.movePrefixTable(prefix, 6)
# print(prefix)
result = solution.strStr("mississippi","issip")
print(result)