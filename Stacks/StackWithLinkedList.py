import Node


class StackWithLinkedList:
    def __init__(self, data):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    def push(self, data):
        temp = Node()
        temp.data = data
        temp.next = self.head
        self.head = temp
        
    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.data
        self.head = self.head.next
        return temp

    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.data
