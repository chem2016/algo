import collections
class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    # stack1: []
    # stack2: [1, 2, 3]
    # stack1: [3, 2, 1]
    def stack2ToStack1(self):
        while self.stack2:
            self.stack1.append(self.stack2.pop())
    
    
    def push(self, element):
        # write your code here
        self.stack2.append(element)

    """
    @return: An integer
    """
    # stack2: [1,2,3]
    # stack1: []
    # after transfer: stack1: [3,2,1], stack2: []
    # pop stack1 directly gives u 1
    def pop(self):
        # write your code here
        if not self.stack1:
            self.stack2ToStack1()
        return self.stack1.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if not self.stack1:
            self.stack2ToStack1()
        return self.stack1[-1]

queue = MyQueue()

queue.push(1)
print(queue.stack1, queue.stack2)

queue.pop()
print(queue.stack1, queue.stack2)

queue.push(2)
print(queue.stack1, queue.stack2)

queue.push(3)
print(queue.stack1, queue.stack2)

queue.top()
print(queue.stack1, queue.stack2)

queue.pop()
print(queue.stack1, queue.stack2)
