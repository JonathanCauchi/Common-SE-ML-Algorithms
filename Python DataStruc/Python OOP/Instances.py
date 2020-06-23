from datetime import date
import itertools


class Employee:
    
    employee_id_count = 0
    raise_amount = 3500
    
    def __init__(self, first,last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '.' + str(date.today().year) + '@gmail.com'
        Employee.employee_id_count += 1
        self.id = self.employee_id_count 
        
    def dispfullname(self):
        print("{} {} {} {}".format(self.first, self.last, self.pay, self.id))
        print("{}".format(self.email))
        
    def applyraise(self):
        self.pay = int(self.pay + self.raise_amount)
    

    
        

emp1 = Employee('Jonathan','Cauchi', 50000)


emp2 = Employee('Jonathan','Cauchi', 50000)

emp3 = Employee('Jonathan','Cauchi', 50000)

emp4 = Employee('Jonathan','Cauchi', 50000)
emp1.dispfullname()
emp2.dispfullname()
emp3.dispfullname()

