class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def __init__(self):
        pass

    def searchBigSortedArray(self, reader, target):
        # write your code here

        endIdx = self.findElementLargerThanTarget(reader, target)

        # binary search target between 0 and endIdx
        start, end = 0, endIdx
        while (start + 1 < end):
            mid = (start + end) // 2
            if reader[mid] > target:
                end = mid
            elif reader[mid] < target:
                start = mid
            else:
                end = mid # want the first match
        
        if reader[start] == target:
            return start
        if reader[end] == target:
            return end
        
        return -1 

    def findElementLargerThanTarget(self, array, target):

        starting = 0
        while(array[starting] < target):
            starting = starting * 2 + 1

        return starting