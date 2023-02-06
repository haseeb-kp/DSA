class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enque(self,data):
        newNode = Node(data)   
        if self.rear is None:
            self.front=self.rear=newNode
            return
        else:
            self.rear.next=newNode
            self.rear=newNode

    def deque(self):
        if self.front is None:
            print("empty queue")
            return
        self.front = self.front.next
        if self.front is None:
            self.rear = None

    def display(self):
        temp=self.front
        if temp is None:
            print("Empty")
            return
        while temp is not None:
            print(temp.data)
            temp=temp.next

newQueue = queue()
newQueue.enque(10)
newQueue.enque(20)
newQueue.enque(30)
newQueue.deque()
newQueue.display()

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None

#     def enqueu(self,data):
#         new_node = Node(data)
#         if self.front is None:
#             self.front = self.rear = new_node
#         else:
#             self.rear.next = new_node
#             self.rear = new_node
#     def dequeue(self):
#         self.front = self.front.next