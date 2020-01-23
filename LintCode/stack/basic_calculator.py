class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def __init__(self):
        pass
    def calculate(self, s):
        # Write your code here

        res, num, sign = 0, 0, 1
        stack = []

        for c in s:
            # for num, get all the digits
            if c.isdigit():
                num = num * 10 + int(c)
            # for left paranthese, push res, and sign onto stack for save, reset res, and sign to 0 and +
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            # for right paranthese, first calculate res with num and sign, then pop out sign and res from stack to update res. then set num = 0 to start fresh
            elif c == ')':
                res = res + sign * num
                num = 0
                res *= stack[-1]
                stack.pop()
                res += stack[-1]
                stack.pop()
            # calculate current result and reset sign and num to 1 and 0
            elif c == '+':
                res = res + sign * num
                num = 0
                sign = 1
            #  calculate current result and reset sign and num to -1 and 0
            elif c == '-':
                res = res + sign * num
                num = 0
                sign = -1
        # when there are number left like +5 at the end we need to add it to current res
        return res + sign * num

solution = Solution()
print(solution.calculate('(1+(4+ 5+2)-3)+(6+8)+5'))