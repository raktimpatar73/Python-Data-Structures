class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    

# driver code
stack = Stack()
stack.push(4)
stack.push(21)
stack.push(46)
stack.push(5)

while not stack.isEmpty():
    print(stack.pop())