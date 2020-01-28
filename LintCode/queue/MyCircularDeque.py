class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque = [0]*k
        self.front = -1
        self.rear = 0
        self.size = k
        
    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear
        self.front = (self.front -1 + self.size) % self.size
        self.deque[self.front] = value

        return True
        

    def insertLast(self, value): 
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear 
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        
        return True

    def deleteFront(self): 
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.arr[self.front] = 0
        self.front = (self.front + 1) % self.size
        if self.front == self.rear:
            self.front = -1
        
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.size) % self.size
        self.deque[self.rear] = 0
        if self.front == self.rear:
            self.front = -1
        
        return True
        

    def getFront(self):
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.deque[self.front]
        

    def getRear(self):
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1 + self.size)%self.size]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == -1
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        """
        return self.rear == self.front


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

circularDeque = MyCircularDeque(3)
print(circularDeque)

print(circularDeque.insertLast(1), "True");			# return true
print(circularDeque.deque, circularDeque.front, circularDeque.rear)
print(circularDeque.insertLast(2), "True");			# return true
print(circularDeque.deque, circularDeque.front, circularDeque.rear)
print(circularDeque.insertFront(3), "True");			# return true
print(circularDeque.deque, circularDeque.front, circularDeque.rear)
print(circularDeque.insertFront(4), "False");			# return false, the queue is full
print(circularDeque.deque, circularDeque.front, circularDeque.rear)
print(circularDeque.getRear(), "2");  			# return 2
print(circularDeque.deque, circularDeque.front, circularDeque.rear)
print(circularDeque.isFull(), "True");				# return true
print(circularDeque.deque, circularDeque.front, circularDeque.rear)
print(circularDeque.deleteLast(), "True");			# return true
print(circularDeque.deque, circularDeque.front, circularDeque.rear)
print(circularDeque.insertFront(4), "True");			# return true
print(circularDeque.deque, circularDeque.front, circularDeque.rear)
print(circularDeque.getFront(), "4");			# return 4
print(circularDeque.deque, circularDeque.front, circularDeque.rear)
