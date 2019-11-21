def removeKthNodeFromEnd(head, k):
    """
    A function that remove from the kth node from the end of a linked list

    sample input: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9, 4
    sample output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9
    """
    total_number = 1
    while(head.next):
        head = head.next
        total_number += 1

    print('total nodes: ', total_number)

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self
    
    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes

myLinkedList = LinkedList(0)
myLinkedList.addMany([1,2,3,4,5,6,7,8,9])
print(myLinkedList.getNodesInArray())

removeKthNodeFromEnd(myLinkedList, 4)