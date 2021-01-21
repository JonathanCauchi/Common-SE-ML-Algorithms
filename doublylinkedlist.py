class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
class LinkedList:
    def __init__(self, root):
        self.root = root        
        self.tail = root
        
    def insert(self,node): #brute force, insertion would take 0(N) time
        current = self.root
        if current.right is None:
            current.right = node
            node.left = current
        else:
            self.insert_node(current.right, node)
    
    def insert_node(self, node, ins_node):
        if node.right:
            self.insert_node(node.right, ins_node)
        else:
            node.right = ins_node
            ins_node.left = node
            
    def efficient_insert(self, node): #Insertion operation only takes O(1) time
        temp = self.tail
        self.tail = node
        self.tail.left = temp
        temp.right = self.tail
            
    def remove(self,node):
        if node.right is None and node.left is not None:
            previous = node.left
            del node
            previous.right = None
        elif node.left is None and node.right is not None:
            next = self.root.right
            del self.root
            next.left = None
            self.root = next.left
        else:
            prev = node.left
            next = node.right
            del node
            prev.right = next
            next.left = prev
        
    def print_links(self, node):
        print("LEFT AND RIGHT VALUES:")
        if(node.left is not None):
            print(node.left.value)
        else:
            print("Node has no left value")
        if(node.right is not None):
            print(node.right.value)
        else:
            print("Node has no right value")
        
    def print_all(self):
        current = self.root
        while(current is not None):
            print(current.value)
            current = current.right
            
    def print_reverse(self):
        current = self.tail
        while(current is not None):
            print(current.value)
            current = current.left
        
        
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
session = LinkedList(node1)
session.efficient_insert(node2)
session.efficient_insert(node3)

#session.print_links(node2)
#session.print_all()

#session.remove(node2)
session.print_all()
#session.print_links(node3)
session.print_reverse()
        