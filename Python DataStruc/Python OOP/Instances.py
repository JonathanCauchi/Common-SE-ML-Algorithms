from datetime import date

class Employee:
    
    def __init__(self, first,last):
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '.' + str(date.today().year) + '@gmail.com'
        
    def dispfullname(self):
        print("{} {}".format(self.first, self.last))
        print("{}".format(self.email))
        
    
        

emp1 = Employee('Jonathan','Cauchi')
emp1.dispfullname()

