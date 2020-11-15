class Node:
    index = 0
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.index = Node.index
        Node.index += 1

class array:
    def __init__(self):
        self.headvalue = None
                 
    def insert_end(self,element):
        new_node = Node(element)
        if self.headvalue == None:
            self.headvalue = new_node
            return
        current = self.headvalue
        while(current.next is not None):
            current = current.next
        current.next = new_node
        
    def insert_begin(self,element):
        new_node = Node(element)
        new_node.next = self.headvalue
        self.headvalue = new_node

    def update(self,element,key):
        current = self.headvalue
        while(current.index != key):
            current = current.next
        current.value = element
        
    def print_list(self):
        current = list.headvalue
        while(current.next is not None):
            print(current.value)
            current = current.next
        print(current.value)
            
        
list = array()
list.headvalue = Node(1)
node2 = Node(2)
node3 = Node(3)
list.headvalue.next = node2
node2.next = node3
list.update(6,2)
list.print_list()
