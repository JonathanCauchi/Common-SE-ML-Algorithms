class string(object):
    
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = input()
        
    def printSting(self):
        print(self.s)

object = string()
object.getString()
object.printSting()