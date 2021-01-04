#not completed yet, just need to add more functionality and add a cool interface somehow
class Node:
    def __init__(self, value, parent):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent 

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        current = self.root
        if current is None:
            self.root = Node(value,None)
        else:
            self.insert_node(value, self.root)
            
    def insert_node(self, value, parent):
        if(value > parent.value):
            if(parent.right is not None):
                self.insert_node(value, parent.right)
            else:
                parent.right = Node(value, parent)
        elif(value < parent.value):
            if(parent.left is not None):
                self.insert_node(value, parent.left)
            else:
                parent.left = Node(value, parent)
        else:
            print("There already exists an entry with that value")
            
    def traverse(self):
        ##answer = input("Enter traversal type 1,2,3..")
        if(self.root is not None):
            self.in_order(self.root)
        else:
            print("Tree is empty!")
            
    def in_order(self, node):
        if(node.left is not None):
            self.in_order(node.left)
        print("%s" %node.value)
        
        if(node.right is not None):
            self.in_order(node.right)
        
    def hard_delete(self, value):
        current = self.root
        if(self.root is not None):
            self.hard_del_imp(value, self.root)
        else:
            print("Tree is empty!")
    
    ## for debugging purposes
    def print_parent(self, value):
        current = self.root
        if(value == self.root.value):
            print("This is the root node, it has no parents")
        elif(value > self.root.value):
            self.print_parent_value(value, self.root.right)
        else:
            self.print_parent_value(value, self.root.left)
            
            
    def print_parent_value(self, value, node):
        parent = node.parent
        if(value > node.value):
            self.print_parent_value(value, node.right)
        elif(value < node.value):
            self.print_parent_value(value, node.left)
        else:
            print("%s" %parent.value)
            
    ## for debugging purposes
    def print_children(self, )
                        
    
    def hard_del_imp(self, value, node):
        if(value == node.value):
            ##Case 1: Leaf Node
            if(node.left and node.right is None):
                parent_leaf = node.parent
                #update parent's pointers
                if(parent_leaf.left == node):
                    parent_leaf.left = None
                if(parent_leaf.right == node):
                    parent_leaf.right = None
                if(parent_leaf is None):
                    self.root = None
                #remove entry
                del node
            
                
        elif(value < node.value):
            self.hard_del_imp(value, node.left)
        else:
            self.hard_del_imp(value, node.right)
            
      
        
        
tree = BST()
tree.insert(8)
tree.insert(4)
tree.insert(12)
tree.insert(17)
tree.insert(45)
tree.print_parent(8)
tree.hard_delete(45)
tree.traverse()
