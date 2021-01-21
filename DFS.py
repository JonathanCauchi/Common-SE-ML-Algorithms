class Node:
    def __init__(self,value):
        self.value = value
        self.adj_list = []
        self.visited = False
        
class DFS:
    def __init__(self):
        print("Started DFS")
        
    def search(self,root):
        #FILO stack ADT is needed
        root.visited = True
        print(root.value)
        for n in root.adj_list:
            if not n.visited:
                self.search(n)
                
if __name__=="__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    
    a.adj_list.append(b)
    
    session = DFS()
    session.search(a)
    
    

                
    