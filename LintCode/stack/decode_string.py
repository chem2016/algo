class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        stack = []
        string = ""
        num = 0
        
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append(string)
                stack.append(num)
                string = ''
                num = 0
            elif c == "]":
                prenum = stack.pop()
                prestring = stack.pop()
                string = prestring + prenum * string
            else:
                print(c)
                print(string)
                string = string + c
        
        return string

solution = Solution()
result = solution.expressionExpand('abc3[e]')
print(result)