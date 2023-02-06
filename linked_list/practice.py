class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.tail = new_node

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end="-->")
            temp = temp.next
    
    def insert_at_end(self,data):
        new_node = node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def insert_after_value(self,data,next_to):
        new_node = node(data)
        temp = self.head
        while temp is not None and temp.data is not next_to:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

        

new_linked_list = linked_list()
# new_linked_list.insert_at_beginning(10)
# new_linked_list.insert_at_beginning(20)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(20)
new_linked_list.insert_at_end(30)
new_linked_list.insert_at_end(40)
new_linked_list.insert_after_value(45, 40)
new_linked_list.insert_after_value(50, 45)
new_linked_list.display()

