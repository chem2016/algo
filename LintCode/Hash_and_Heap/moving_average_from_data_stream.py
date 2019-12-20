class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.arr = []
        self.size = size
        self.total = 0
    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        if len(self.arr) < self.size:
            self.total += val
            self.arr.append(val)
            return self.total / len(self.arr)
        else:
            self.total += val
            self.arr.append(val)
            self.total -= self.arr.pop(0)
            return self.total / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)