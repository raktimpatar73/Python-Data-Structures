class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
        
#driver code

queue = Queue()
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(57)
queue.enqueue(45)
queue.enqueue(10)

while not queue.isEmpty():
    print(queue.dequeue())