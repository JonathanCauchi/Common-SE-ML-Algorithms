class Queue: #FIFO
    array = [] #either array or linkedlist
    length = 0
    def __init__(self):
        print("Queue is initialized")
        
    def enqueue(self,value):
        self.isunique(value)
        self.array.append(value)
        self.length += 1
        
    def dequeue(self):
        del self.array[0]
        
    def isunique(self,value):
        for i in self.array:
            if(i==value):
                return False
            else:
                return True
        
    def print_queue(self):
        for i in self.array:
            print(i)
            
session = Queue()
session.enqueue(1)
session.enqueue(2)
session.enqueue(3)
session.print_queue()
session.dequeue()
session.print_queue()

        