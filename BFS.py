class Node:
    def __init__(self, value):
        self.value = value
        self.adj_list = []
        self.visited = False
    
class BFS:
     def __init__(self):
       print("Starting BFS")
        
     def search(self, root):
       queue = []
       queue.append(root)
       while queue:
          
           node = queue[0]
           del queue[0]
           node.visited = True
           print(node.value)
          
           for i in node.adj_list:
               if i.visited is False:
                   queue.append(i)
                    
if __name__ == "__main__":
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    
    nodeA.adj_list.append(nodeB)
    nodeA.adj_list.append(nodeC)
    nodeB.adj_list.append(nodeD)
    
    session = BFS()
    session.search(nodeA)
    
  
    

            
        
        