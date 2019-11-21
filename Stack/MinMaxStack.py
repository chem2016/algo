class MinMaxStack:

    def __init__(self):
        # self.minMaxStack = []
        self.stack = []

    def peek(self):

        return self.stack[0]

    def pop(self):
        
        return self.stack.pop(0)

    def push(self, number):
        
        self.stack.insert(0, number)
        
    def getMin(self):

        return min(self.stack)
        

    def getMax(self):
        
        return max(self.stack)