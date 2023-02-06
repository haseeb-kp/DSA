class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,data):
        newNode = Node(data)    
        if self.head is None:
            self.head=newNode
        else:
            self.tail.next=newNode
        self.tail=newNode

    def insertAtBegining(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            temp = self.head
            self.head = newnode
            newnode.next = temp
    
    def delete(self,data):
        temp = self.head

        # in head case
        if temp is not None and temp.data is data:
            self.head=temp.next
            return

        # not in head case
        while temp is not None and temp.data is not data:
            prev=temp
            temp=temp.next
        
        if temp is None:
            return
        # temp none means LL finished. Thus error may occur

        # if last element is removing, tail will be removed, Thus..
        if temp is self.tail:
            tail=prev
            tail.next=None
            return

        prev.next = temp.next
        

    def insertAfterElement(self,nextTo,data):
        newNode=Node(data)
        temp = self.head

        while temp is not None and temp.data is not nextTo:
            temp=temp.next

            if temp is None:
                return

            if temp is self.tail:
                self.tail.next=newNode
                self.tail=newNode
                return
            
        newNode.next = temp.next
        temp.next = newNode
    
    def display(self):
        if self.head is None:
            print("empty")
            return

        tempNode = self.head

        while tempNode is not None:
            print(tempNode.data,end=""+"-->")
            tempNode = tempNode.next
        print("END")

newlinkedlist = linkedList()
newlinkedlist.addNode(10)
newlinkedlist.addNode(20)
# newlinkedlist.insertAtBegining(5)
# newlinkedlist.insertAtBegining(1)
# newlinkedlist.delete(10)
# newlinkedlist.insertAfterElement(10, 30)
newlinkedlist.display()


