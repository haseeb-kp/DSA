class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp.data

class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, data):
        self.stack1.push(data)

    def dequeue(self):
        if self.stack2.head is None:
            while self.stack1.head is not None:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
    

new_queue = Queue()
new_queue.enqueue(10)
new_queue.enqueue(20)
new_queue.enqueue(30)
print(new_queue.dequeue())