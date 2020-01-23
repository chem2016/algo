class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        # corner case
        if s == "":
            return True
        left_parantheses = "([{"
        right_parantheses = ")]}"
        stack = []
        
        for char in s:
            if left_parantheses.find(char) != -1:
                stack.append(char)
            else:
                right_index = right_parantheses.find(char)
                if len(stack) == 0:
                    return False
                left_index = left_parantheses.find(stack[-1])
                if right_index == left_index:
                    stack.pop()
                    continue
                return False
        
        return len(stack) == 0