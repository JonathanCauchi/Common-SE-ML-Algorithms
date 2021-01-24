class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
        
class AVL:
    def __init__(self):
        self.root = None
        
    def insert(self, node):
        current = self.root
        if current is None:
            current = node
        else:
            self.insert_node(current, node)
            
    def insert_node(self, current, node):
        
        if(node < current):
            if(current.left is None):
                current.left = node
                node.parent = current
                node.height = max(self.calculate_height(node.left),self.calculate_height(node.right)) + 1
            else:
                self.insert_node(current.left)
        else:
            if(current.right is None):
                current.right = node
                node.parent = current
                node.height = max(self.calculate_height(node.left),self.calculate_height(node.right)) + 1
            else:
                self.insert_node(current.right)
        
        self.check_balance(node)

    def remove(self, node):
        if self.root:
            self.remove_node(node, self.root)
            
    def remove_node(self, node, current):
        if current is None:
            print("Node is inxistent")
            return False
        if node.data < current.data:
            self.remove_node(node, current.left)
        elif node.data > current.data:
            self.remove_node(node, current.right)
        else:
            
        #got bored, the rest is easy to solve
            
    #def traverse(self):
            
    #def inorder
            
    #def preorder
            
    #def postorder
        

    def calculate_height(self, node):
        if node is None:
            return -1
        return node.height
    
    def calculate_balance(self,node):
        if node is None:
            return 0
        return self.calculate_height(node.left) - self.calculate_height(node.right)
        
    
    def check_violation(self, node):
        while node is not None:
            node.height = max(self.calculate_height(node.left),self.calculate_height(node.right)) + 1
            self.violation_helper(node)
            node = node.parent
            
    def violation_helper(self,node):
        
        balance = self.calculate_balance(node)
        
        if balance > 1:
            # left heavy, right rotation
            if(self.check_balance(node.left) < 0):
                self.left_rotation(node.left)
                
            self.right_rotation(node)
            
        if balance < -1:
            # right heavy, left rotation
            if(self.calculate_balance(node.right) > 0):
                self.right_rotation(node.right)     
        
            self.left_rotation(node)        
        
    def right_rotation(self, node):
            
        temp1 = node.left
        temp2 = node.left.right
        temp3 = node.parent
            
            
        node.parent = temp1
        temp1.right = node
        node.left = temp2
        temp1.parent = temp3 
        
        #updating pointer references
        if temp2:
            temp2.parent = node
        if temp1.parent is not None and temp1.parent.left == node:
            temp1.parent.left = temp1
        if temp1.parent is not None and temp1.parent.right ==node:
            temp1.parent.right = temp1
        if node == self.root:
            self.root = temp1
                
        temp1.height = max(self.calculate_height(temp1.left),self.calculate_height(temp1.right)) + 1
        node.height = max(self.calculate_height(node.left),self.calculate_height(node.right)) + 1
            
    def left_rotation(self, node):
        
        temp1 = node.right
        temp2 = node.right.left
        temp3 = node.parent
        
        node.parent = temp1
        temp1.left = node
        node.right = temp2
        temp1.parent = temp3
        
        #updating pointer references
        if temp2:
            temp2.parent = node
        if node.parent is not None and node.parent.right == node:
            node.parent.right = temp1
        if node.parent is not None and node.parent.left == node:
            node.parent.left = temp1
        if node.parent == self.root:
            self.rooot = temp1
            
        temp1.height = max(self.calculate_height(temp1.left),self.calculate_height(temp1.right)) + 1
        node.height = max(self.calculate_height(node.left),self.calculate_height(node.right)) + 1
        
if __name__ =="__main__":
    node1 = Node(1)
    node2 = Node(-1)
    node3 = Node(2)
    session = AVL()
    session.insert(node1)
    session.insert(node2)
    session.insert(node3)