class Solution:
    def __init__(self):
        pass
    def splitString(self, s):
        res = []
        if s == None:
            return res
        if len(s) == 0:
            res.append([])
            return res
        self.dfs(res, [], 0, s)

        return res

    def dfs(self, res, cur, index, s):
        if index >= len(s):
            res.append(cur)
            return
        i = index
        while(i < index + 2 and i < len(s)):
            sub = s[index:i+1]
            cur.append(sub)
            self.dfs(res, cur, i+1, s)
            cur.pop(len(cur)-1)
            i += 1

solution = Solution()
result = solution.splitString('123')
print(result)