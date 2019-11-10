def balancedBrackets(string):
    """
    Sample input "([])(){}()"
    """
    stack = []
    balance_dict = {
        "(": ")",
        ")":"(",
        "[":"]",
        "]":"[",
        "{":"}",
        "}":"{"
    }
    for char in string:
        stack.insert(0, char)
        key = char
        if len(stack) > 1:
            value = stack[1]
            if balance_dict[key] == value:
                stack.pop(0)
                stack.pop(0)
    
    if len(stack) != 0:
        return False
    else:
        return True

sample_input = """([])(){}()"""
print(balancedBrackets(sample_input))