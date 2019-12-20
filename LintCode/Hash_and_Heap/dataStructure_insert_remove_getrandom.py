from random import randint
class RandomizedSet:
    
    def __init__(self):
        # do intialization if necessary
        # use hashmap to keep track of element positon (val -> position) for swapping to remove empty hole in array after remove
        self.arr = []
        self.hashMap = {}
        self.hashSet = set()

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if val not in self.hashSet:
            self.arr.append(val)
            self.hashSet.add(val)
            self.hashMap[val] = len(self.arr) - 1
            return True
        return False

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val in self.hashSet:
            self.hashSet.remove(val)
            val_index = self.hashMap[val]
            last_index = len(self.arr) - 1
            self.swap(val_index, last_index)
            self.arr.pop()
            del self.hashMap[val]
            return True
        else:
            return False
            
    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        return self.arr[randint(0, len(self.arr)-1)]
        
    def swap(self, index1, index2):
        self.arr[index1] = self.arr[index2]
        self.hashMap[self.arr[index2]] = index1


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()