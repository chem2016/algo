import collections

class Stack:
    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()
    
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.queue1.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        while(len(self.queue1) > 1):
            element = self.queue1.popleft()
            self.queue2.append(element)
        if self.queue1:
            self.queue1.popleft()
        self.swap()
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        while(len(self.queue1) > 1):
            element = self.queue1.popleft()
            self.queue2.append(element)
        
        retEle = self.queue1.popleft()
        self.swap()
        self.queue1.append(retEle)  # you need to put this back since top is liking peek it move change you stack
        return retEle

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        if len(self.queue1) == 0:
            return True
        else:
            return False
        
    def swap(self):
        # help1
        self.queue1, self.queue2 = self.queue2, self.queue1
# stack = Stack()
# print('stack1: ', stack.queue1, stack.queue2)
# stack.push(1)
# print('stack2: ', stack.queue1, stack.queue2)
# stack.pop()
# print('stack3: ', stack.queue1, stack.queue2)
# stack.push(2)
# print('stack4: ', stack.queue1, stack.queue2)
# stack.isEmpty()
# print('stack5: ', stack.queue1, stack.queue2)
# stack.top()
# print('stack6: ', stack.queue1, stack.queue2)
# stack.pop()
# print('stack7: ', stack.queue1, stack.queue2)
# stack.isEmpty()
# print('stack8: ', stack.queue1, stack.queue2)
stack = Stack()
print('stack1: ', stack.queue1, stack.queue2)
stack.push(1)
print('stack2: ', stack.queue1, stack.queue2)
stack.push(2)
print('stack3: ', stack.queue1, stack.queue2)
stack.pop()
print('stack4: ', stack.queue1, stack.queue2)
print(stack.top())
print('stack5: ', stack.queue1, stack.queue2)