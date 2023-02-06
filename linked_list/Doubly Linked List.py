class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class doublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def addNode(self,data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode

        else:
            self.tail.next = newNode
            newNode.prev = self.tail

        self.tail = newNode

    def addelement(self,data,nextTo):
        newNode =Node(data)
        temp=self.head

        while(temp is not None and temp.data is not nextTo):
            temp=temp.next
        newNode.next=temp.next
        temp.next=newNode
        newNode.prev=temp
        newNode.next.prev=newNode

    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=""+"<-->")
            temp=temp.next
        print("END")

    def displayReverse(self):
        temp = self.tail
        while temp is not None:
            print(temp.data,end=""+"<-->")
            temp=temp.prev
        print("END")

dLL=doublyLinkedList()
dLL.addNode(10)
dLL.addNode(20)
dLL.addNode(30)
dLL.addelement(25, 20)
dLL.display()
dLL.displayReverse()