class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.minStack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        if len(self.stack) == 0:
            self.stack.append(number)
            self.minStack.append(number)
        else:
            if number < self.minStack[-1]:
                self.stack.append(number)
                self.minStack.append(number)
            else:
                self.stack.append(number)
                self.minStack.append(self.minStack[-1])

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if len(self.stack) == 0:
            return
        self.minStack.pop()
        return self.stack.pop()

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        return self.minStack[-1]