class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def distinct_power_1(self): # using the most intuitive approach
        powers = []
        for i in range(self.a, self.b+1):
            for j in range(self.a, self.b+1):
                powers.append(i**j)
        final_list = []
        for i in powers:
            if i not in final_list:
                final_list.append(i)
        print(len(final_list))
                   
    def distinct_power_2(self): # using list comprehension
        powers = []
        for i in range(self.a, self.b+1):
            for j in range(self.a, self.b+1):
                powers.append(i**j)
        final_list = []
        [final_list.append(x) for x in powers if x not in final_list]
        print(len(final_list))
        
    def distinct_power_3(self): # using set()
        powers = []
        for i in range(self.a, self.b+1):
            for j in range(self.a, self.b+1):
                powers.append(i**j)
        print(len(set(powers)))
        
    #def distinct_power_3(self):
        
session = A(2,100)
session.distinct_power_1()

