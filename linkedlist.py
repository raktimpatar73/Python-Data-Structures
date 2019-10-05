class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def remove(self, data, previous):
        if self.data == data:
            previous.next = self.next
            del self.data
            del self.next
        else:
            if self.next is not None:
                self.next.remove(data, self) 

class LinkedList:
    def __init__(self):
        self.head = None
        self.counter = 0

    def insertStart(self, data):
        self.counter += 1
        newnode = Node(data)
        if not self.head:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def size(self):
        return self.counter

    def insertEnd(self, data):
        if not self.head:
            self.insertStart(data)
            return
        self.counter+=1 
        newnode = Node(data)
        current = self.head

        while current.next != None:
            current = current.next
        
        current.next == newnode

    def remove(self, data):
        
        if self.head:
            if data == self.head.data:
                self.counter -= 1
                self.head = self.head.next
            else:
                self.head.remove(data, self.head)

    def traverse(self):
        current = self.head
        while current!=None:
            print(current.data)
            current = current.next

# driver code

linkedlist = LinkedList()
linkedlist.insertStart(15)
linkedlist.insertStart(12)
linkedlist.insertStart(31)
linkedlist.insertStart(21)

linkedlist.traverse()
linkedlist.remove(31)
linkedlist.traverse()