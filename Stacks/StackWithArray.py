class StackWithArray:
    def __init__(self, Capacity = 1):
        self.top = 1
        self.Capacity = Capacity
        self.A = [None]*Capacity

    def push(self, data):
        if self.Capacity == self.top + 1:
            print("Stack overflow")
            return
        self.top += 1
        self.A[self.top] = data

    def pop(self):
        if self.top == -1:
            print ("Stack underflow")
            return
        temp = self.A[self.top]
        self.top -= 1
        return temp
    
    def peek(self):
        if self.top == - 1:
            print ("Stack underflow")
            return
        return self.A[self.top]
    
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.Capacity == self.top + 1
    
