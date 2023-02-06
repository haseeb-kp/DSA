class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None
    
    def push(self,data):
        newNode = Node(data)   
        if self.top is None:
            self.top=newNode
        else:
            newNode.next=self.top
            self.top=newNode

    def pop(self):
        if self.top is None:
            print('stack underflow')
            return
        else:
            n = self.top
            self.top=self.top.next
            return n.data
    
    def display(self):
        temp=self.top
        if temp is None:
            print("Empty")
            return
        while temp is not None:
            print(temp.data)
            temp=temp.next

newStack=stack()
newStack.push(10)
newStack.push(20)
newStack.push(30)
newStack.display()
print("-----")
print(newStack.pop())
# newStack.display()




'''class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None
    
    def push(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is not None:
            self.top = self.top.next
    def peak(self):
        print(self.top.data)
    def display(self):
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next

new_stack = stack()
new_stack.push(10)
new_stack.push(20)
new_stack.push(30)
new_stack.pop()
new_stack.display()
new_stack.peak()'''