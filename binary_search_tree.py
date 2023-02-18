class Node:
    def __init__(self, data,left=None, right=None):
        self.left = None
        self.right = None
        self.data = data
        
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        current_node = self.root
        if current_node is None:
            self.root = Node(data)
            return
        while True:
            if data < current_node.data:
                if current_node.left is None:
                    current_node.left = Node(data)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = Node(data)
                    break
                else:
                    current_node = current_node.right

    def contains(self,data):
        current_node = self.root
        while current_node is not None:
            if data < current_node.data:
                current_node = current_node.left
            elif data > current_node.data:
                current_node = current_node.right
            else:
                return True
        return False
    
    def remove(self,data):
        self.remove_helper(data,self.root,parent_node=None)

    def remove_helper(self,data,current_node,parent_node):
        while current_node is not None:
            if data < current_node.data:
                parent_node = current_node
                current_node = current_node.left
            elif data > current_node.data:
                parent_node = current_node
                current_node = current_node.right
            else:
                if current_node.left is not None and current_node.right is not None:
                    current_node.data = self.get_min_value(current_node.right)
                    self.remove_helper(current_node.data,current_node.right,current_node)
                else:
                    if parent_node is None:
                        if current_node.right is None:
                            self.root = current_node.left
                        else:
                            self.root = current_node.right
                    else:
                        if parent_node.left == current_node:
                            if current_node.right is None:
                                parent_node.left = current_node.left
                            else:
                                parent_node.left = current_node.right
                        else:
                            if current_node.right is None:
                                parent_node.right = current_node.left
                            else:
                                parent_node.right = current_node.right
                break

    def get_min_value(self,current_node):
        if current_node.left is None:
            return current_node.data
        else:
            return self.get_min_value(current_node.left)

    def get_max_value(self,current_node):
        if current_node.right is None:
            return current_node.data
        else:
            return self.get_min_value(current_node.right)

    

    def in_order(self):
        self.in_order_helper(self.root)
    
    def in_order_helper(self,node):
        if node is not None:
            self.in_order_helper(node.left)
            print(node.data, end=" ")
            self.in_order_helper(node.right)

    def pre_order(self):
        self.pre_order_helper(self.root)
    
    def pre_order_helper(self,node):
        if node is not None:
            print(node.data, end=" ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    def post_order(self):
        self.post_order_helper(self.root)
    
    def post_order_helper(self,node):
        if node is not None:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            print(node.data, end=" ")

    def level_order(self):
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            curr = queue.pop(0)
            print(curr.data)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    def find_closest(self,target):
        current_node = self.root
        closest = current_node.data
        while current_node is not None:
            if abs(target - closest) > abs(target - current_node.data):
                closest = current_node.data
            if target < current_node.data:
                current_node = current_node.left
            elif target > current_node.data:
                current_node = current_node.right
            else:
                break
        return closest

    def validate_bst(self):  #O(n)T , O(d)S
        return self.validate_bst_helper(self.root,float('-inf'),float('inf'))

    def validate_bst_helper(self,node,min_value,max_value):
        if node is None:
            return True
        if node.data < min_value or node.data >= max_value:
            return False
        is_left_valid = self.validate_bst_helper(node.left, min_value, node.data)
        is_right_valid = self.validate_bst_helper(node.right, node.data, max_value)
        return is_left_valid and is_right_valid
        


tree = BinarySearchTree()
tree.insert(50)
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(60)
tree.insert(70)
# print(tree.validate_bst())
# tree.level_order()
# print("in order traversal")
# tree.remove(4)
tree.in_order()
print("in order traversal")
tree.pre_order()
print("pre order traversal")
tree.post_order()
print("post order traversal")
# print(tree.find_closest(12))

'''root= Node(10, 
                left=Node(5, 
                              left=Node(2), 
                              right=Node(7)
                             ), 
                right=Node(15, 
                               right=Node(22)
                              )
               )
root = Node(5,left=Node(1),right=Node(4,left=Node(3),right=Node(6)))

print("result =", tree.validate_bst(root))'''










'''def in_order_traversal(self, root):
    result = []
    if root:
        result = self.in_order_traversal(root.left)
        result.append(root.data)
        result = result + self.in_order_traversal(root.right)
    return result'''
