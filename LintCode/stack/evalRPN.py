class Solution:
    """
    @param tokens: The Reverse Polish Notation
    @return: the value
    """
    def evalRPN(self, tokens):
        # write your code here
        if len(tokens) == 0:
            return 0
        stack = []
        for token in tokens:
            if token == "+":
                number2, number1 = stack.pop(), stack.pop()
                stack.append(number1 + number2)
            elif token == "-":
                number2, number1 = stack.pop(), stack.pop()
                stack.append(number1 - number2)
            elif token == "*":
                number2, number1 = stack.pop(), stack.pop()
                stack.append(number1 * number2)
            elif token == "/":
                number2, number1 = stack.pop(), stack.pop()
                sign = 1 if number1 * number2 > 0 else -1
                stack.append(sign*(abs(number1) // abs(number2)))
            else:
                stack.append(int(token))
        
        return stack[0]