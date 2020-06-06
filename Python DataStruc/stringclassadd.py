class string(object):
    
    def __init__(self):
        self.s = "Love and "
    
    def inputString(self):
        string = input()
        self.s = self.s + string
        
    
    def printStrng(self):
        print(self.s)
        
object = string()
object.printStrng()
object.inputString()
object.printStrng()