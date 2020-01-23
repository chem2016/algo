class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        # record key corresponds to the node which next is your current node, in order to op on LL
        self.key_to_prev = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.key_to_prev:
            return -1
        self.kick(self.key_to_prev[key])
        return self.key_to_prev[key].next.value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.value = value
            return
        self.push_back(LinkedNode(key, value))
        if len(self.key_to_prev) > self.capacity:
            self.pop_front()
    
    def kick(self, prev):
    # change "prev->node-next-> ...->tail"
    # to "prev-next-> ..->tail->node"
    
        node = prev.next
        if node == self.tail:
            return
        prev.next = node.next
        self.key_to_prev[node.next.key] = prev
        node.next = None
        self.push_back(node)
    
    def push_back(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node
    
    def pop_front(self):
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy
    
    
class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


    
